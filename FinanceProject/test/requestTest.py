import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.conf import settings
from FinanceProject.db.dao.ScrapyDao import wacai_handle_Qry,Content_Qry,Domin_Qry
class jsonRequestSpider(scrapy.Spider):
    name = 'jsonRequest'
    allowed_domains = Domin_Qry()
    start_urls = []
    for item in Content_Qry()['ST']:
        start_urls.append(item[1])
    # print('start_urls=',start_urls)
    # start_urls.append('http://www.xiaoniu88.com/product/investment');
    rules = []
    for rule in Content_Qry()['RE']:
        rules.append(Rule(LinkExtractor(allow=(rule[2])),rule[5],follow=rule[3]))

    def start_requests(self):
        start_urls = []
        for item in Content_Qry()['ST']:
            start_urls.append(item[1])
        for url in start_urls :#= 'https://m.wukonglicai.com/weixin/recommendPageInfo.html'
            yield scrapy.Request(url,self.parse)

    def parse(self,response):
        print("response = ",response.text)

from scrapy.crawler import CrawlerProcess
if __name__ == "__main__":
    process = CrawlerProcess(settings)
    spiders = jsonRequestSpider()
    process.crawl(spiders)
    process.start()