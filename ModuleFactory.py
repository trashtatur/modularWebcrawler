from spiders.RegisteredModules import REGISTERED_MODULES
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import logging

logger = logging.getLogger(__name__)
runner = CrawlerRunner(get_project_settings())


def run_all_modules():
    configure_logging()
    for module in REGISTERED_MODULES:
        try:
            runner.crawl(module)
            logger.debug(module.name + " succesfully loaded")
        except:
            logger.critical("Module " + module.name + " could not be started")

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)
    d.close()


def stop_all_modules():
    runner.stop()


if __name__ == '__main__':
    run_all_modules()
