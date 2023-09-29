import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags

def remove_currency(value):
    #     KES28,000,000
    return value.replace('KSh', '')

def remove_commas(value):
    value = remove_currency(value)
    return value.replace(',', '')

def try_float(value):
    try:
        return float(value)
    except ValueError:
        return value


class BrParentItem(scrapy.Item):
    house_href = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    
    house_price = scrapy.Field(
        input_processor=MapCompose(remove_tags,str.strip, remove_commas, try_float),
        output_processor=TakeFirst()
    )

    house_location = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )    




class BrChildItem(scrapy.Item):


    service_type = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )

    property_type = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )

    bed_rooms = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip, int),
        output_processor=TakeFirst()
    )    

  