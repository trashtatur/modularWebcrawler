from spiders.RegisteredModules import REGISTERED_MODULES
from scrapy.utils.log import configure_logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import logging

logger = logging.getLogger(__name__)


def run_all_modules():

    process = CrawlerProcess(get_project_settings())
    configure_logging()

    for module in REGISTERED_MODULES:
        try:
            process.crawl(module)
            logger.debug(module.name+" succesfully loaded")
        except:
            logger.critical("Module " + module.name + " could not be started")

    process.start()


