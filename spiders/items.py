# -*- coding: utf-8 -*-

# Define here the models for your scraped items
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class MetaItems(Item):
    datetime = Field()  # post time
    url = Field()  # tweet url


class PostContent(Item):
    text = Field()  # text content
    user = Field()  # username of tweet


class Main(Item):
    postContent = Field(serializer=PostContent)
    meta = Field(serializer=MetaItems)
    siteSpecific = Field(serializer="SiteSpecific")


####################


class MainLoader(ItemLoader):
    default_item_class = Main
    default_output_processor = TakeFirst()


class MetaItemsLoader(ItemLoader):
    default_item_class = MetaItems
    default_output_processor = TakeFirst()


class PostContentLoader(ItemLoader):
    default_item_class = PostContent
    default_output_processor = TakeFirst()
