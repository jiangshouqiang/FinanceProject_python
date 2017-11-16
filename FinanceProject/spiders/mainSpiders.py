from scrapy.spiders import CrawlSpider,Rule,Request
from scrapy.linkextractors import LinkExtractor
from FinanceProject.items import FinanceprojectItem,FinanceMapItem
from FinanceProject.log.FinanceLogger import FinanceLogger
from FinanceProject.db.dao.ScrapyDao import main_handle_Qry,Content_Qry,Domin_Qry
from FinanceProject.spiders.parse.wukong import wukong_json
from FinanceProject.spiders.parse.wacai import wacai_parse
from scrapy.conf import settings
from FinanceProject.tool.Validator import deleteUrl

class main_spider(CrawlSpider):
    name = "mainSpider"

    # 加载初始爬取连接
    def start_requests(self):
        # 解析抓去的页面信息
        for start_url in Content_Qry()['ST']:
            yield Request(start_url[1],eval(start_url[5]))


from scrapy.crawler import CrawlerProcess
if __name__ == "__main__":
    #删除URL存储对象
    deleteUrl()
    process = CrawlerProcess(settings)
    spiders = main_spider()
    process.crawl(spiders)
    process.start()