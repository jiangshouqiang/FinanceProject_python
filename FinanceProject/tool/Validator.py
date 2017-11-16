from FinanceProject.db.dao.ScrapyDao import Domin_Qry
from FinanceProject.db.dao.ScrapyDao import main_handle_Qry,Scrapy_content_re,Scrapy_sub_cloumn
from FinanceProject.log.FinanceLogger import FinanceLogger
from FinanceProject.tool.RedisUtil import sadd,delObj

@FinanceLogger()
def isCountine(response):
    # 记录URL已被处理
    result = sadd(response.url)
    return result == 1

@FinanceLogger()
def deleteUrl():
    # 删除URL记录
    result = delObj("url")
    return result == 1

# 验证URL是否为允许处理的域内
@FinanceLogger()
def domainValidator(key:str,val:str):
    allowed_domains = Domin_Qry()
    for domain in allowed_domains:
        part = val.find(domain)
        if (part > -1):
            return True
    return False

# 过滤已处理的URL
