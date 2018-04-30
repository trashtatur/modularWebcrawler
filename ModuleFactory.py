from spiders.RegisteredModules import REGISTERED_MODULES
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import logging

logger = logging.getLogger(__name__)


def run_all_modules():
    configure_logging()
    runner = CrawlerRunner(get_project_settings())
    for module in REGISTERED_MODULES:
        try:
            runner.crawl(module)
            logger.debug(module.name + " succesfully loaded")
        except:
            logger.critical("Module " + module.name + " could not be started")

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)
