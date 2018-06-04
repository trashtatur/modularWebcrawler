# README FOR WEBCRAWLER

- Dependancies : 
    - Install with ``pip install -r requirements.txt --user``
     
## Start the App

### Directly

- cd to the root folder of the webcrawler
- Execute ``python -m frontend.frontend.py``
- Open your browser and go to ``http://0.0.0.0:5000``

### With Docker

- cd to the root folder of the webcrawler
- execute ``docker build -t webcrawler:latest .``
- execute ``docker run -it -p 5000:5000 webcrawler`` 
- Open your browser and go to ``http://0.0.0.0:5000``

## Create a Module

To create a module you must create a new python package in ``webcrawler/spiders``.
Name it any way you want. It hast to contain a class that implements one of Scrapies
Crawler interfaces like ``CrawlSpider`` or so.

To make it work with the webcrawler, import the following into the modules spider:
``from spiders.RegisteredModules import REGISTERED_MODULES, register_module``

Then put ``@register_module`` above the classname.

If the module implements a method that scrapie can recognize, such as ``parse`` or ``start_requests`` it should start
fine.

Since modules must implement the name variable we shall make use of it:

Modules are required to implement the following variable in the ``__init__``
function of the crawler:
```python
from SearchStrings import SEARCHSTRINGS
from spiders.settings import custom_settings
class Module:
    name="NAME"
    custom_settings = custom_settings
    def __init__(self):
        self.query = SEARCHSTRINGS[Module.name]

```
its important to reference the module name and pull it from the ``SEARCHSTRINGS``
collection! The instance variable itself can have any name. Its important
where it gets its data from!

The Custom settings import and declaration makes the spider able to work and
not to be blocked by remote sites! So do that.

The Spider does not have to be named "NAME". That is just an example!

For further information look at the twitter module

## Documentation

Twitter Module pretty much copied from : https://github.com/jonbakerfish/TweetScraper

Scrapy Documentation: https://doc.scrapy.org/en/latest/

## Module Output

A Module should always output in the following format:
```json
{
  "postContent":{
    "user": "USERNAME",
    "text":"RAW TEXT",
    "cleanText": "CLEANED TEXT"
  },
  "meta": {
    "URL": "http://www.heinz-wackelpudding.de",
    "dateTime":"11.11.2011",
    "lang":"en"
  },
  "siteSpecific":{
    "MODULENAME":{
      "here":"bla",
      "are":"bla",
      "some":"bla",
      "site Specific":"bla",
      "informations":"bla",
      "like":"bla",
      "retweets":"bla"
    }
  },
  "sentimentData": {
    "Whatever":"bla",
    "needs":"bla",
    "to":"bla",
    "be":"bla",
    "here":"bla!!!"
  }
}

```
This output can be ensured by defining items and itemloaders according to this format
In the following examples ``MODULENAME`` is to be replaced with the actual Modulename!!!
```python
from spiders.items import Item, ItemLoader, TakeFirst, Field


class MODULENAMESpecific(Item):
    ID = Field()  # tweet id
    user_id = Field()  # user id
    retweets = Field()  # nbr of retweet
    favorites = Field()  # nbr of favorite
    replies = Field()  # nbr of reply


class SiteSpecific(Item):
    Twitter = Field(serializer=MODULENAMESpecific)


#############


class MODULENAMESpecificLoader(ItemLoader):
    default_item_class = MODULENAMESpecific
    default_output_processor = TakeFirst()


class SiteSpecificLoader(ItemLoader):
    default_item_class = SiteSpecific
    default_output_processor = TakeFirst()
```

And then, such items can be populated in the following way

```python
from spiders.items import MetaItemsLoader, PostContentLoader, MainLoader
from spiders.twitter.items import SiteSpecificLoader, MODULENAMESpecificLoader

main = MainLoader()
post_content = PostContentLoader()
meta = MetaItemsLoader()
siteSpecific = SiteSpecificLoader()
MODULENAMESpecific = MODULENAMESpecificLoader()


siteSpecific.add_value('MODULENAME', twitterSpecific.load_item())
main.add_value('siteSpecific', siteSpecific.load_item())
main.add_value('postContent', post_content.load_item())
main.add_value('meta', meta.load_item())

yield main.load_item()
```