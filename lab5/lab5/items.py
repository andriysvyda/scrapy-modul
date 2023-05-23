import scrapy


class EkatalogItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    shop = scrapy.Field()
    price = scrapy.Field()

