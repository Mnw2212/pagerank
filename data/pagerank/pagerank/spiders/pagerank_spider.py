from scrapy.spider import Spider
from scrapy.selector import Selector

class PagerankSpider(Spider):
	name = "pagerank"
	allowed_domains = ["wikipedia.org"]
	start_urls = [
		"http://en.wikipedia.org/wiki/Main_Page"
		]


	def parse(self, response):
		sel =Selector(response)
		sites = sel.xpath('//ul/li')
		for site in sites:
			title = site.xpath('a/text()').extract()
			link = site.xpath('a/@href').extract()
			desc = site.xpath('text()').extract()
			print title, link, desc
