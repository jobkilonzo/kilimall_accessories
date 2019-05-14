import scrapy

class KilimallSpider(scrapy.Spider):
    name="kilimall"

    start_urls = [
        'https://www.kilimall.co.ke/phones-accessories/'
    ]

    def parse(self, response):
        for accessories in response.xpath("//li[@class='item']"):
            yield{
                'name': accessories.xpath(".//h2[@class='goods-name']/a/text()").extract_first(),
                'price': accessories.xpath(".//div[@class='goods-price']/em/text()").extract_first()
            }

            next_page= response.selector.xpath("//li/a[@class='demo']/@href").extract_first()

            if next_page is not None:
                next_page_link = response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)
