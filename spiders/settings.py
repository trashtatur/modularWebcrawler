custom_settings = {
    "BOT_NAME": 'MoodCrawler',
    "SPIDER_MODULES": ['webcrawler.spiders'],
    "NEWSPIDER_MODULE": 'webcrawler.spiders',
    "USER_AGENT": "Googlebot",
    "ROBOTSTXT_OBEY": True,
    "LOG_LEVEL": 'INFO',
    "DOWNLOAD_DELAY": 2,
    "ITEM_PIPELINES": {
        'pipelines.ConsolePipe': 100
    }
}