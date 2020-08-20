# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewsItem(scrapy.Item):
    user = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
    review = scrapy.Field()