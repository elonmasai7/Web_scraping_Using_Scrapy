import scrapy
from countries_gdp.items import CountryGdpItem
from scrapy.loader import ItemLoader


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        #Css Selectors
        # for country in response.css('table.wikitable.sortable tbody tr:not([class])'): #css selectors; select that tr that in that table that doesnthave a class
        #     item = CountryGdpItem()
        #     item["country_name"] = country.css('td:nth-child(1) a::text').get()
        #     item["region"] = country.css('td:nth-child(2) a::text').get()
        #     item["gdp"] =  country.css('td:nth-child(3)::text').get()
        #     item["year"] = country.css('td:nth-child(4)::text').get()
        #     yield item
        #xpath

        # for country in response.xpath("//table[contains(@class, 'wikitable sortable')]//tbody//tr"):
        #     yield {
        #         "country_name": country.xpath(".//td[1]//a/text()").get(),
        #         "region": country.xpath(".//td[2]//a/text()").get(),
        #         "gdp": country.xpath(".//td[3]/text()").get(),
        #         "year": country.xpath(".//td[4]/text()").get(),
        #     }


        #Improve your item loading
        for country in response.css('table.wikitable.sortable tbody tr:not([class])'):
            item = ItemLoader(item= CountryGdpItem(), selector = country)
            # item.add_value("country_name", "United States")
            item.add_css("country_name", "td:nth-child(1) a")
            item.add_css("region", "td:nth-child(2) a")
            item.add_css("gdp", "td:nth-child(3)")
            item.add_css("year", "td:nth-child(4)")   

            yield item.load_item()            