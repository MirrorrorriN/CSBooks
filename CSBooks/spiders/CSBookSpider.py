# -*- coding: utf-8 -*-
import scrapy
import re
from CSBooks.items import CsbooksItem

# 解决 Python2.x版本中乱码问题，Python3.x 版本中不需要
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
global pageNo
class CSBookSpider(scrapy.Spider):
    name = "CSBooks"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=0&type=T',
    )

    # def start_requests(self):
    #     yield Request("https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA?start=0&type=T",headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"})

    def parse(self,response):
        tmp=response.xpath('/html/body/div[@id="wrapper"]/div[@id="content"]/div/div/div')
        context=tmp.xpath('./ul')
        books=context.xpath('./li/div[@class="info"]')
        for i in xrange(len(books)):
            book=books[i]
            title=book.xpath('./h2/a/@title').extract_first()
            score=book.xpath('./div/span[@class="rating_nums"]/text()').extract_first()
            print title
            
            item=CsbooksItem()
            if title:
                item['title']=title
            if score:
                item['score']=score
            item['tag']='推理'
            yield item

        nextPage=tmp.xpath('./div[@class="paginator"]/span[@class="next"]/a/@href').extract_first()
        if nextPage:
            baseUrl='https://book.douban.com'
            page = baseUrl + nextPage
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        
    