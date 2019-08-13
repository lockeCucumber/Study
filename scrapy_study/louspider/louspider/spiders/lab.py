# -*- coding: utf-8 -*-
import scrapy
from louspider.items import MingyanItem


class LabSpider(scrapy.Spider):
    name = 'lab'

    def start_requests(self):
        url = 'http://lab.scrapyd.cn/'
        tag = getattr(self, 'tag')
        if tag:
            url = url + '/tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        mingyan = response.css('div.quote')
        for v in mingyan:
            item = MingyanItem()
            item['text'] = v.css('.text::text').extract_first()
            item['author'] = mingyan.css('small::text').extract_first()
            tags = v.css('.tags .tag::text').extract()
            item['tags'] = tags
            yield item

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)

