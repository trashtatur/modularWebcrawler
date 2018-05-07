from spiders.items import Item, ItemLoader, TakeFirst, Field


class TwitterSpecific(Item):
    ID = Field()  # tweet id
    user_id = Field()  # user id
    retweets = Field()  # nbr of retweet
    favorites = Field()  # nbr of favorite
    replies = Field()  # nbr of reply


class SiteSpecific(Item):
    Twitter = Field(serializer=TwitterSpecific)


#############


class TwitterSpecificLoader(ItemLoader):
    default_item_class = TwitterSpecific
    default_output_processor = TakeFirst()


class SiteSpecificLoader(ItemLoader):
    default_item_class = SiteSpecific
    default_output_processor = TakeFirst()