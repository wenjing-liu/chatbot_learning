import sys

import scrapy
from w3lib.html import remove_tags
from subtitle_spider.items import SubtitleSpiderItem

class SubtitleSpider(scrapy.Spider):
  name = 'subtitle'
  allowed_domains = ['zimuku.net']
  start_urls = [
      "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=20",
      "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=21",
      "http://www.zimuku.net/search?q=&t=onlyst&ad=1&p=22"
    ]

  def parse(self, response):
    herfs = response.selector.xpath('//div[contains(@class, "persub")]/h1/a/@href').extract()
    for herf in herfs:
      url = response.urljoin(herf)
      request = scrapy.Request(url, callback=self.parse_detail)
      yield request

  def parse_detail(self, response):
    url = response.selector.xpath('//li[contains(@class, "dlsub")]/div/a/@href').extract()[0]
    print('processing:', url)
    request = scrapy.Request(url, callback=self.parse_file)
    yield request

  def parse_file(self, response):
    body = response.body
    item = SubtitleSpiderItem()
    item['url'] = response.url
    item['body'] = body
    return item


