# -*- coding: utf-8 -*-
import scrapy
import re

# 解决 Python2.x版本中乱码问题，Python3.x 版本中不需要
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class CSBookSpider(scrapy.Spider):
    name = "CSBooks"
    allowed_domains = ["douban.com"]
    start_urls = (
        'https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA?start=0&type=T',
    )
    pageNo=0

    # def start_requests(self):
    #     yield Request("https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA?start=0&type=T",headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"})

    def parse(self,response):
        context=response.xpath('/html/body/div[@id="wrapper"]/div[@id="content"]/div/div/div/ul').extract()
        for node in context:
            
            # print 'x'
            print "doubanSpiderTest"+node
        if self.pageNo<=1:
            self.pageNo+=1
            baseUrl='https://book.douban.com/tag/%E8%AE%A1%E7%AE%97%E6%9C%BA?start='
            page = baseUrl + str(self.pageNo*20)+'type=T'
            print page
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        
    