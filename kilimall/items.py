import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_quotation(value):
    return value.replace(u"\u201d",'').replace(u"\u201c", '')

class KilimallItem(scrapy.Item):
    name= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotation),
        output_processor= TakeFirst()
    )
    price= scrapy.Field(
        input_processor= MapCompose(str.strip, remove_quotation),
        output_processor= TakeFirst()
    )
