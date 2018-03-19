# -*- coding: utf-8 -*-
import scrapy
#if it could not run, pls "pip install pypiwin32"
class BooksSpider(scrapy.Spider):
    name = 'books'
    # 定义了起始url，运行爬虫后会自动下载
    start_urls = ['http://books.toscrape.com/']
    def parse(self, response):
        # 分析目标页面的 html 节点构造，循环遍历列表，获取相应的数据。
        for book in response.css('article.product_pod'):
            name = book.xpath('./h3/a/@title').extract_first()
            price = book.css('p.price_color::text').extract_first()
            yield {
                'name':name,
                'price':price
            }
            # 解析下一个需要爬取的页面
            next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
            if next_url:
                next_url = response.urljoin(next_url)
                yield scrapy.Request(next_url, callback=self.parse)


