import scrapy
from glo.items import GloItem
from scrapy.loader import ItemLoader

class GlorealtorsSpider(scrapy.Spider):
    name = "glorealtors"
    allowed_domains = ["glorealtors.com"]
    start_urls = ["https://glorealtors.com/search-results/?status%5B0%5D&areas%5B0%5D&keyword"]
    page_number = 1  # Initialize the page number

    def parse(self, response):
        for house in response.css('div.item-listing-wrap'):
            item = ItemLoader(item=GloItem(), selector=house)
            item.add_css("house_href", "div.item-body h2 > a::attr(href)")
            yield item.load_item()

        # Check for the "Next" button
        next_page = response.css('ul.pagination li.page-item.active + li.page-item a.page-link::attr(href)').extract_first()
        if next_page:
            self.page_number += 1
            yield scrapy.Request(url=next_page, callback=self.parse)
