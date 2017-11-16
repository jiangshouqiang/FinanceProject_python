# from scrapy.spiders import CrawlSpider,Rule
# from scrapy.linkextractors import LinkExtractor
from FinanceProject.items import FinanceprojectItem,FinanceMapItem
from FinanceProject.log.FinanceLogger import FinanceLogger
from FinanceProject.db.dao.ScrapyDao import main_handle_Qry,Scrapy_content_re,Scrapy_sub_cloumn
from FinanceProject.tool.Validator import isCountine,domainValidator
from scrapy import Request
import json
import re
import redis

# 挖出分配到的ID为3
@FinanceLogger()
def wukong_json(response):
    # print(response.text)
    # 该URL是否已被处理
    if not isCountine(response):
        return
    # 筛选域名限制
    # if not domainValidator(response.url):
    #     return
    # 获取URL匹配正则表达式
    content_re = Scrapy_content_re([3,])
    for content in content_re:
        url_re = content[2]
        urlList = re.findall(url_re,response.text)
        for url in urlList:
            yield Request(url,url_re[5])
    try:
        responseJson = json.loads(response.text)
    except Exception as ex:
        print(ex)
        return
    itemMap = FinanceMapItem()
    financeMap = []
    cloumnMap = {}
    if cloumnMap is not None or len(cloumnMap) < 1:
        cloumnMap = main_handle_Qry([3,])
    start_cloumns = cloumnMap["RT"]
    for start_cloumn in start_cloumns:
        sub_cloumn = Scrapy_sub_cloumn([start_cloumn[8],])
        for value in responseJson[start_cloumn[1]]:
            item = FinanceprojectItem()
            print("value = ",value,", type = ",type(value))
            for cloumn in sub_cloumn:
                if cloumn[2] is not None and cloumn[2] is not '':
                    item[cloumn[0]] = [cloumn[2],]
                else:
                    item[cloumn[0]] = [value[cloumn[1]],]
            financeMap.append(item)
        print("financeMap = ",financeMap)
        itemMap['financeMap'] = financeMap
        yield itemMap