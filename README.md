# README FOR WEBCRAWLER

- Dependancies : ``scrapie``

## Create a Module

To create a module you must create a new python package in ``webcrawler/spiders``.
Name it any way you want. It hast to contain a class that implements one of Scrapies
Crawler interfaces like ``CrawlSpider`` or so.

To make it work with the webcrawler, import the following into the modules spider:
``from spiders.RegisteredModules import REGISTERED_MODULES, register_module``

Then put ``@register_module`` above the classname.

If the module implements a method that scrapie can recognize, such as ``parse`` or ``start_requests`` it should start
fine.

For further information look at the twitter module

## Documentation

Twitter Module pretty much copied from : https://github.com/jonbakerfish/TweetScraper

Scrapy Documentation: https://doc.scrapy.org/en/latest/