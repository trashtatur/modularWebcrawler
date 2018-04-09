from _datetime import datetime
from urllib.parse import quote
from spiders.twitter.items import Tweet
import json
import logging
from scrapy.spiders import CrawlSpider
from scrapy import http, Selector

from spiders.RegisteredModules import REGISTERED_MODULES, register_module

logger = logging.getLogger(__name__)


@register_module
class TwitterSpider(CrawlSpider):
    name = "TwitterSpider"

    def __init__(self, *a, **kwargs):
        super().__init__(*a, **kwargs)
        self.lang = "en"
        self.url = "https://twitter.com/i/search/timeline?l={}".format(self.lang)
        self.url += "&q=%s&src=typed&max_position=%s"

    def start_requests(self):
        url = self.url % (quote("#maga"), '')
        yield http.Request(url, callback=self.parse_page)

    def parse_page(self, response):

        data = json.loads(response.body.decode("utf-8"))
        for item in self.parse_tweets_block(data['items_html']):
            yield item

        min_position = data['min_position']
        url = self.url % (quote("#maga"), min_position)
        yield http.Request(url, callback=self.parse_page)

    def parse_tweets_block(self, html_page):
        page = Selector(text=html_page)

        items = page.xpath('//li[@data-item-type="tweet"]/div')
        for item in self.parse_tweet_item(items):
            yield item


    def parse_tweet_item(self,items):
        for item in items:
            try:
                tweet = Tweet()

                tweet['usernameTweet'] = \
                    item.xpath('.//span[@class="username u-dir u-textTruncate"]/b/text()').extract()[0]

                ID = item.xpath('.//@data-tweet-id').extract()
                if not ID:
                    continue
                tweet['ID'] = ID[0]

                ### get text content
                tweet['text'] = ' '.join(
                    item.xpath('.//div[@class="js-tweet-text-container"]/p//text()').extract()).replace(' # ',
                                                                                                        '#').replace(
                    ' @ ', '@')
                if tweet['text'] == '':
                    # If there is not text, we ignore the tweet
                    continue

                ### get meta data
                tweet['url'] = item.xpath('.//@data-permalink-path').extract()[0]

                retweets = item.css('span.ProfileTweet-action--retweet > span.ProfileTweet-actionCount').xpath(
                    '@data-tweet-stat-count').extract()
                if retweets:
                    tweet['retweets'] = int(retweets[0])
                else:
                    tweet['retweets'] = 0

                favorites = item.css('span.ProfileTweet-action--favorite > span.ProfileTweet-actionCount').xpath(
                    '@data-tweet-stat-count').extract()
                if favorites:
                    tweet['favorites'] = int(favorites[0])
                else:
                    tweet['favorites'] = 0

                replies = item.css('span.ProfileTweet-action--reply > span.ProfileTweet-actionCount').xpath(
                    '@data-tweet-stat-count').extract()
                if replies:
                    tweet['replies'] = int(replies[0])
                else:
                    tweet['replies'] = 0

                tweet['datetime'] = datetime.fromtimestamp(int(
                    item.xpath('.//div[@class="stream-item-header"]/small[@class="time"]/a/span/@data-time').extract()[
                        0])).strftime('%Y-%m-%d %H:%M:%S')

                yield tweet

            except:
                logger.error("Error tweet:\n%s" % item.xpath('.').extract()[0])
