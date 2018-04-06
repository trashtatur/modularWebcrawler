import scrapy
from spiders.RegisteredModules import REGISTERED_MODULES,register_module


@register_module
class TwitterSpider(scrapy.Spider):
    name = "TwitterSpider"
    start_urls = ["https://twitter.com/hashtag/maga"]

    def define_urls(hashtags):
        start_urls = []
        for hashtag in hashtags:
            start_urls.append("https://twitter.com/hashtag/" + str(hashtag))
        return start_urls

    def parse(self, response):
        for tweet in response.css('div.content'):
            yield {
                'text': tweet.css('p.tweet-text').extract_first()
            }
