import os
import signal
from scrapy import Spider
from SearchStrings import SEARCHSTRINGS
from spiders.RegisteredModules import REGISTERED_MODULES
from scrapy.utils.log import configure_logging
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import logging

logger = logging.getLogger(__name__)


def run_all_modules():
    sorted_modules = cullModules()

    configure_logging()
    if len(sorted_modules) is not 0:
        runner = CrawlerRunner(get_project_settings())
        for module in sorted_modules:
            try:
                bla = issubclass(module, Spider)
                if bla:
                    runner.crawl(module)
                    logger.debug(module.name + " succesfully loaded")
                else:
                    module.run()
                    logger.debug(module.name + " succesfully loaded")
            except:
                logger.critical("Module " + module.name + " could not be started")

        d = runner.join()
        d.addBoth(lambda _: reactor.stop())
        reactor.run(installSignalHandlers=False)

    else:
        logger.debug("No modules enabled, try again")


def stop_all_modules():
    os.kill(os.getpid(), signal.SIGKILL)


def cullModules():
    return [module for module in REGISTERED_MODULES if module.name in SEARCHSTRINGS]
