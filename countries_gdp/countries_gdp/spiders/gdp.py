import scrapy


class GdpSpider(scrapy.Spider):
    name = "gdp"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"]

    def parse(self, response):
        for country in response.css('table.wikitable.sortable tbody tr'): #css selectors
            yield {
                "country_name": country.css('td:nth-child(1) a::text').get(),
                "region": country.css('td:nth-child(2) a::text').get(),
                "gdp": country.css('td:nth-child(3) ::text').get(),
                "year": country.css('td:nth-child(4) ::text').get(),
                
            }
