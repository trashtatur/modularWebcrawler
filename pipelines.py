# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from flask_socketio import emit


class ConsolePipe:

    def process_item(self, item, spider):
        emit('//PRINTED_STUFF', str(item))
