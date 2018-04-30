# README FOR WEBCRAWLER

- Dependancies : 
    - Install with ``pip install -r requirements.txt --user``
    
     ``scrapy``
    
     ``flask``
     
     ``pika``
     
## Start the App
- cd to the root folder of the webcrawler
- Execute ``python -m frontend.frontend.py``
- Open your browser and go to ``localhost:5000/``

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
"some": "some",
"keys": "keys",
"here": "here",

"meta": {
    "someOther": "someOther",
    "keysOrSo": "keysOrSo",
    "hereOrWhat": "hereOrWhat"
    }
}
```
This output can be ensured by defining items and itemloaders according to this format

```python
from scrapy import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class MetaItem(Item):
    some = Field()
    key = Field()
    here = Field()


class MainItem(Item):
    some = Field()
    key = Field()
    here = Field()
    meta = Field(serializer = MetaItem)


class MainLoader(ItemLoader):
    default_item_class = MainItem
    default_output_processor = TakeFirst()


class MetaLoader(ItemLoader):
    default_item_class = MetaItem
    default_output_processor = TakeFirst()
```

And then, such items can be populated in the following way

```python
import MetaLoader
import MainLoader
main:MainLoader  = MainLoader()
meta = MetaLoader()
main.add_value('key', value)
meta.add_value('key', value)
main.add_value('meta', meta.load_item())
yield main.load_item()
```