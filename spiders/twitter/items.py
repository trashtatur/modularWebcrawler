# -*- coding: utf-8 -*-

# Define here the models for your scraped items
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class MetaItems(Item):
    ID = Field()  # tweet id
    datetime = Field()  # post time
    user_id = Field()  # user id
    retweets = Field()  # nbr of retweet
    favorites = Field()  # nbr of favorite
    replies = Field()  # nbr of reply
    url = Field()  # tweet url


class Tweet(Item):
    usernameTweet = Field()  # username of tweet
    text = Field()  # text content
    meta = Field(serializer=MetaItems)


class TweetLoader(ItemLoader):
    default_item_class = Tweet
    default_output_processor = TakeFirst()


class MetaItemsLoader(ItemLoader):
    default_item_class = MetaItems
    default_output_processor = TakeFirst()
