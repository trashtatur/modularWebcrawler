from _datetime import datetime
from urllib.parse import quote
from spiders.items import MetaItemsLoader, PostContentLoader, MainLoader
from spiders.twitter.items import SiteSpecificLoader, TwitterSpecificLoader
from spiders.rabbitMQPipe import RabbitMQPipeline
import json
import logging
from scrapy.spiders import CrawlSpider
from scrapy import http, Selector
from SearchStrings import SEARCHSTRINGS
from spiders.settings import custom_settings

from spiders.RegisteredModules import register_module

logger = logging.getLogger(__name__)
rabbit = RabbitMQPipeline()


@register_module
class TwitterSpider(CrawlSpider):
    name = "TwitterSpider"
    custom_settings = custom_settings

    def __init__(self):
        self.lang = "en"
        self.query = SEARCHSTRINGS[TwitterSpider.name]
        self.url = "https://twitter.com/i/search/timeline?l={}".format(self.lang)
        self.url += "&q=%s&src=typed&max_position=%s"

    def start_requests(self):
        url = self.url % (quote(self.query), '')
        yield http.Request(url, callback=self.parse_page)

    def parse_page(self, response):

        data = json.loads(response.body.decode("utf-8"))
        for item in self.parse_tweets_block(data['items_html']):
            yield item

        min_position = data['min_position']
        url = self.url % (quote(self.query), min_position)
        yield http.Request(url, callback=self.parse_page)

    def parse_tweets_block(self, html_page):
        page = Selector(text=html_page)

        items = page.xpath('//li[@data-item-type="tweet"]/div')
        for item in self.parse_tweet_item(items):
            yield item

    def parse_tweet_item(self, items):
        for item in items:
            try:
                main = MainLoader()
                post_content = PostContentLoader()
                meta = MetaItemsLoader()
                siteSpecific = SiteSpecificLoader()
                twitterSpecific = TwitterSpecificLoader()

                username_tweet = \
                    item.xpath('.//span[@class="username u-dir u-textTruncate"]/b/text()').extract()[0]

                post_content.add_value('user', username_tweet)
                ### get text content

                text = ' '.join(
                    item.xpath('.//div[@class="js-tweet-text-container"]/p//text()')
                        .extract()) \
                    .replace(' # ', '#')\
                    .replace(' @ ', '@')

                if text == '':
                    # If there is not text, we ignore the tweet
                    continue
                post_content.add_value('text', text)

                ### get twitterSpecific data -----------------------------------------------

                ID = item.xpath('.//@data-tweet-id').extract()
                if not ID:
                    continue
                twitterSpecific.add_value('ID', ID)

                retweets = item.css('span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount')\
                    .xpath('@data-tweet-stat-count')\
                    .extract()
                if retweets:
                    twitterSpecific.add_value('retweets', int(retweets[0]))
                else:
                    twitterSpecific.add_value('retweets', 0)

                favorites = item.css('span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount')\
                    .xpath('@data-tweet-stat-count')\
                    .extract()

                if favorites:
                    twitterSpecific.add_value('favorites', int(favorites[0]))
                else:
                    twitterSpecific.add_value('favorites', 0)

                replies = item.css('span.ProfileTweet-action--reply > span.ProfileTweet-actionCount')\
                    .xpath('@data-tweet-stat-count')\
                    .extract()

                if replies:
                    twitterSpecific.add_value('replies', int(replies[0]))
                else:
                    twitterSpecific.add_value('replies', 0)

                ### get meta data -----------------------------------------------

                url = item.xpath('.//@data-permalink-path').extract()[0]
                meta.add_value('url', url)

                date_time = datetime.fromtimestamp(int(
                    item.xpath('.//div[@class="stream-item-header"]/small[@class="time"]/a/span/@data-time')
                        .extract()[0]))\
                    .strftime('%Y-%m-%d %H:%M:%S')

                meta.add_value('datetime', date_time)
                # BUILD ITEM
                siteSpecific.add_value('Twitter', twitterSpecific.load_item())
                main.add_value('siteSpecific', siteSpecific.load_item())
                main.add_value('postContent', post_content.load_item())
                main.add_value('meta', meta.load_item())

                #yield main.load_item()
                rabbit.process_item(main.load_item())

            except:
                logger.error("Error tweet:\n%s" % item.xpath('.').extract()[0])
