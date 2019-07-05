import scrapy

class SandoSpider(scrapy.Spider):
    name = 'sando'
    start_urls = [
        'https://www.reddit.com/r/brandonsanderson',
    ]

    used_urls = {}

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)