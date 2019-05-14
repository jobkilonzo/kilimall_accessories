import scrapy
from scrapy.loader import ItemLoader
from kilimall.items import KilimallItem

class KilimallSpider(scrapy.Spider):
    name="kilimall"

    start_urls = [
        'https://www.kilimall.co.ke/phones-accessories/'
    ]

    def parse(self, response):
        for accessories in response.xpath("//li[@class='item']"):

            loader= ItemLoader(item=KilimallItem(), selector=accessories, response=response)
            loader.add_xpath('name', ".//h2[@class='goods-name']/a/text()")
            loader.add_xpath('price', ".//div[@class='goods-price']/em/text()")
            yield loader.load_item()

            next_page= response.selector.xpath("//li/a[@class='demo']/@href").extract_first()

            if next_page is not None:
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)
