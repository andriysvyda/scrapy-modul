import scrapy
from bs4 import BeautifulSoup
from lab5.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from lab5.items import EkatalogItem
import time

class EkatalogSpider(scrapy.Spider):
    name = "ekatalog"
    allowed_domains = ["ek.ua"]
    start_urls = ["https://ek.ua/ua/list/63/"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=10
            )

    def parse(self, response):
        soup = BeautifulSoup(response.body,  "html.parser")
        productList = soup.find(id = "list_form1")
        for product in productList:
            if product:
                name = product.find(class_ = "model-short-title no-u").find(string=True, recursive=False)
                url = product.find(class_ = "model-short-info").get("href")
                image = product.find(class_ = "list-zoomer").find(class_ = "img id").find(string=True, recursive=False)
                shop = product.find(class_ = "model-shop-name").find(class_ = "sn-div").find(string=True, recursive=False)
                price = product.find(class_ = "model-shop-price").find(string=True, recursive=False)
                yield EkatalogItem(
                        name = name,
                        url = url,
                        image = image,
                        price = price,
                        shop = shop,
                    )
