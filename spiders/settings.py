custom_settings = {
    "BOT_NAME": 'MoodCrawler',
    "SPIDER_MODULES": ['webcrawler.spiders'],
    "NEWSPIDER_MODULE": 'webcrawler.spiders',
    "USER_AGENT": 'webcrawler (www.yourcoon.de) by HAW Hamburg germany',
    "ROBOTSTXT_OBEY": True,
    "LOG_LEVEL": 'INFO',
    "DOWNLOAD_DELAY": 2,
    "ITEM_PIPELINES": {
        #'webcrawler.pipelines.RabbitMQPipeline':100
        #'webcrawler.pipelines.WebcrawlerPipeline': 300,
    }
}