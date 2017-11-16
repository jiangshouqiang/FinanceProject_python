from FinanceProject.items import FinanceprojectItem,FinanceMapItem
from FinanceProject.log.FinanceLogger import FinanceLogger
from FinanceProject.tool.Validator import isCountine,domainValidator
from FinanceProject.db.dao.ScrapyDao import Scrapy_content_re,main_handle_Qry,Scrapy_sub_cloumn


from scrapy import Request
import re

# 全局URL记录对象
global haveUrl
haveUrl = []
@FinanceLogger()
def wacai_parse(response):

    # 该URL是否已被处理
    if not isCountine(response):
        return
    # 筛选域名限制
    # if not domainValidator(response.url):
    #     return
    # 获取域名
    domain_complie = re.compile("([http:\/\/|https:\/\/].*\.\w+)")
    domain = domain_complie.search(response.url).group(1)
    content_re = Scrapy_content_re([1,])
    for content in content_re:
        url_re = content[2]
        urlList = re.findall(url_re,response.text)
        for url in urlList:
            part = url.find(domain)
            if part < 0:
                url = domain + url
            print(url," = ",content[5])
            yield Request(url,eval(content[5]))

    itemMap = FinanceMapItem()
    financeMap = []
    cloumnMap = {}

    if cloumnMap is not None or len(cloumnMap) < 1:
        cloumnMap = main_handle_Qry([1,])

    start_cloumns = cloumnMap["RT"]
    for start_cloumn in start_cloumns:
        sub_cloumn = Scrapy_sub_cloumn([start_cloumn[8],])
        for value in response.xpath(start_cloumn[1]):
            item = FinanceprojectItem()
            item['from_url'] = response.url
            for cloumn in sub_cloumn:
                if cloumn[2] is not None and cloumn[2] is not '':
                    item[cloumn[0]] = cloumn[2]
                else:
                    if cloumn[3] is not None and cloumn[3] is not '':
                        item[cloumn[0]] = value.xpath(cloumn[1])[0].re(cloumn[3])
                    else:
                        item[cloumn[0]] = value.xpath(cloumn[1]).extract()

            financeMap.append(item)
        itemMap['financeMap'] = financeMap
        yield itemMap

