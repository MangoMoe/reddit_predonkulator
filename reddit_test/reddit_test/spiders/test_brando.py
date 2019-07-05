# -*- coding: utf-8 -*-
import scrapy


class TestBrandoSpider(scrapy.Spider):
    name = 'test_brando'
    # TODO do we need to modify this?
    allowed_domains = ['www.reddit.com']
    start_urls = ['https://www.reddit.com/r/brandonsanderson/']

    def __init__(self):
        self.reddit_prefix = 'https://www.reddit.com'

    def start_requests(self):
        # TODO figure out if this is redundant
        urls = ['https://www.reddit.com/r/brandonsanderson/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_stream)

    def parse_stream(self, response):
        # so this is the things we are looking at in the page
        links_to_follow = set()
        print("GETTING LINKS--------------")
        # for link in response.xpath('//a'):
        for link in response.css('a::attr("href")'):
            if "brandonsanderson/comments" in link.get():
                if not "http" in link.get():
                    links_to_follow.add(self.reddit_prefix + link.get())
                else:
                    links_to_follow.add(link.get())
            if len(links_to_follow) > 50:
                break

        print("PRINTING LINKS--------------")
        # print(links_to_follow)
        for link in links_to_follow:
            print(link)
            yield response.follow(link, self.parse_post)

    def parse_post(self, response):
        print("PARSE POST---------------")
        yield {"thing": "does this work?",}
