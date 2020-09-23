# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field, Item

# class ScrapingUrlItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class ScrapingUrlItem(Item):
    # define the fields for your item here like:
    Title = Field()
    Url = Field()
    Votes = Field()
