import scrapy


class TwitterSpider(scrapy.Spider):
    name = "TwitterSpider"
    start_urls = []

    def __init__(self, hashtags, **kwargs):
        super().__init__(**kwargs)
        self.hashtags = hashtags
        self.start_urls = self.define_urls()

    def define_urls(self):
        start_urls = []
        for hashtag in self.hashtags:
            start_urls.append("https://twitter.com/hashtag/" + str(hashtag))
        return start_urls

    def parse(self, response):
        for tweet in response.css('div.content'):
            yield {
                'text': tweet.css('p.tweet-text').extract_first()
            }
