# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from FinanceProject.db.dao.ScrapyDao import Scrapy_Update

class FinanceprojectPipeline(object):
    def process_item(self, item, spider):
        if item is not None and len(item['financeMap'])>0 :

            Scrapy_Update(item)
        return item
