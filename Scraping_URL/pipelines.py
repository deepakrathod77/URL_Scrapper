# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

# class ScrapingUrlPipeline:
#     def process_item(self, item, spider):
#         return item

class ScrapingUrlPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = self.conn['Scraping_URL']
        self.urlTitle = db['urlTitle']
        self.urlMetadata = db['urlMetadata']


    def process_item(self, item, spider):
        self.urlTitle.insert({"Url":item['Url'], "Title":item['Title']})
        self.urlMetadata.insert({"Url":item['Url'],"Title":item['Title'],"Votes":item['Votes']})
