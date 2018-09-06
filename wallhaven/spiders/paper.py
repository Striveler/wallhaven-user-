# -*- coding: utf-8 -*-
import scrapy
from wallhaven.items import WallhavenItem

#第一种方法

class PaperSpider(scrapy.Spider):
    name = 'paper'
    allowed_domains = ['alpha.wallhaven.cc']
    offset = 1
    link = "https://alpha.wallhaven.cc/favorites?page="

    def start_requests(self):
        url = 'https://alpha.wallhaven.cc/auth/login'
    	yield scrapy.FormRequest(
                url = url,
                formdata = {"_token":"o1W1M5Tx1heUP9c1iPw7ZHPrLhWg2KFc1EJrZNds","username":"striveler@gmail.com","password":"FWB19951208"},
                callback = self.parse
            )

    def parse(self, response):
        #print '-------------1------------'+response.url
        #offset = 1
        #link = "https://alpha.wallhaven.cc/favorites?page="
        url = self.link + str(self.offset)
        yield scrapy.Request(url,callback = self.parse_newpage)

    def parse_newpage(self,response):
        item = WallhavenItem()
        for i in response.xpath('//a[@class="preview"]/@href').extract():
           yield scrapy.Request(i,callback=self.parse_item)
           
        if 1 < 2 :
            self.offset += 1

    def parse_item(self,response):
        item = WallhavenItem()
        link = response.xpath('//html/body/main/section/div[@class="scrollbox"]/img/@src').extract()
        url = ''.join(link)
        urls = "https:"+url
        item['urls'] = urls

        yield item
        yield scrapy.Request(self.link+str(self.offset),callback=self.parse_newpage)


#第二种方法
"""
class PaperSpider(scrapy.Spider):
    name = 'paper'
    allowed_domains = ['alpha.wallhaven.cc']
    start_urls = (
        'https://alpha.wallhaven.cc/auth/login',
        )

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
                response,
                formdata = {"username":"striveler@gmail.com","password":"FWB19951208"},
                callback = self.parse_page
            )

    def parse_page(self,response):
        print "-------------------1----------" + response.url
        url = 'https://alpha.wallhaven.cc/favorites?page=1'
        yield scrapy.Request(url,callback=self.parse_newpage)

    def parse_newpage(self,response):
        print "---------------2------------" + response.url
        with open('test.html','w') as filename:
            filename.write(response.body)

"""




