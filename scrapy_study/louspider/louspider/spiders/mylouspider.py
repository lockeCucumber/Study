import scrapy
from louspider.items import CourseItem
from scrapy.selector import Selector

class LouSpider(scrapy.Spider):
    name = "mylouspider"
    # 定义允许的域名
    allowed_domains = ["shiyanlou.com"]
    # 定义进行爬取的url列表
    start_urls = ['https://www.shiyanlou.com/courses/?category=all&course_type=all&tag=all&fee=free']

    # 另外一种初始链接写法,一般用start_urls更方便
    # def start_requests(self):
    #     urls = [ #爬取的链接由此方法通过下面链接爬取页面
    #         'http://lab.scrapyd.cn/page/1/',
    #         'http://lab.scrapyd.cn/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)


    # 解析并提取Item对象
    def parse(self, response):
        hxs = Selector(response)
        courses = hxs.xpath('//div[@class="col-md-3 col-sm-6  course"]')
        for course in courses:
            item = CourseItem()
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract()[0].strip()
            item['learned'] = course.xpath('.//span[@class="course-per-num pull-left"]/text()').extract()[1].strip()
            item['image'] = course.xpath('.//div[@class="course-img"]/img/@src').extract()[0].strip()
            yield item

        next_page = hxs.xpath('//div//li/a[@aria-label="Next"]/@href').extract_first()
        self.log(next_page)
        if next_page != "#":
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, self.parse)
