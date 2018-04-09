# -*- coding: utf-8 -*-

# Define here the models for your scraped items
from scrapy import Item, Field


class Tweet(Item):
    ID = Field()       # tweet id
    url = Field()      # tweet url
    datetime = Field() # post time
    text = Field()     # text content
    user_id = Field()  # user id
    usernameTweet = Field() # username of tweet

    retweets = Field()  # nbr of retweet
    favorites = Field() # nbr of favorite
    replies = Field()    # nbr of reply
