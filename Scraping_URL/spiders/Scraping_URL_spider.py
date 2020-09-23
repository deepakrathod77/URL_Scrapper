import scrapy
from Scraping_URL.items import ScrapingUrlItem
from scrapy import Spider

class Scraping_URL_Spider(Spider):
    name = "Scraping_URL"
    start_urls = ['https://news.ycombinator.com/']


    def parse(self, response):

        items = ScrapingUrlItem()

        titles = response.css('.athing')
        subtexts = response.css('.subtext')

        for i in range(0,len(titles)-1):
            Title = titles.css('.storylink::text')[i].extract()
            Url = titles.css('.storylink::attr(href)')[i].extract()
            Votes = subtexts.css('.score::text')[i].extract() if subtexts.css('.score::text')[i] != None else ()

            items['Title'] = Title
            items['Url'] = Url
            items['Votes'] = Votes

            yield items
