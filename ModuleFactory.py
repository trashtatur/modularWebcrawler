import os
import signal

from scrapy.exceptions import CloseSpider

from SearchStrings import SEARCHSTRINGS
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
    for module in cullModules():
        try:
            runner.crawl(module)
            logger.debug(module.name + " succesfully loaded")
        except:
            logger.critical("Module " + module.name + " could not be started")

    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run(installSignalHandlers=False)


def stop_all_modules():
    os.kill(os.getpid(), signal.SIGSTOP)


if __name__ == '__main__':
    run_all_modules()


def cullModules():
    return [module for module in REGISTERED_MODULES if module.name in SEARCHSTRINGS]
