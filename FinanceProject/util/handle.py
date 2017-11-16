from FinanceProject.db.dao.ScrapyDao import Scrapy_content_re
from FinanceProject.log.FinanceLogger import FinanceLogger
from FinanceProject.spiders.parse.wacai import wacai_parse
from FinanceProject.spiders.parse.wukong import wukong_json

from scrapy import Request
import re

@FinanceLogger()
def next_handle(response,content_id:[]):
    # 获取域名
    domain_complie = re.compile("([http:\/\/|https:\/\/].*\.\w+)")
    domain = domain_complie.search(response.url).group(1)
    content_re = Scrapy_content_re(content_id)
    print("domain2 = ",domain)
    for content in content_re:
        url_re = content[2]
        urlList = re.findall(url_re,response.text)
        print("urlList = ",urlList)
        for url in urlList:
            part = url.find(domain)
            if part < 0:
                url = domain + url
            print(url," = ",content[5])
            yield Request(url,eval(content[5]))