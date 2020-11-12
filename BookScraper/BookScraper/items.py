# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class BookScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    episode_notes_link = Field()
    
