from spiders.RegisteredModules import REGISTERED_MODULES
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess


def build_all_modules():
    print("BLA")

    for module in REGISTERED_MODULES:
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
        })
        configure_logging()
        process.crawl(module)
        process.start()


build_all_modules()
