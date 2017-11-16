# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item,Field


class FinanceprojectItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    domain     = Field() #域名
    organ      = Field() #机构标示
    fin_name   = Field() #理财产品名称
    pro_bate   = Field() #产品年化收益
    user_num   = Field() #投资用户数量
    begin_amt  = Field() #启投金额
    pro_cycle  = Field() #理财周期
    pro_size   = Field() #产品购买人数
    pro_all_amt= Field() #产品总量
    pro_can_amt= Field() #产品剩余总量
    buy_button = Field() #申购按键
    buy_url    = Field() #申购链接
    pro_flag   = Field() #产品标示
    from_url   = Field() #数据来源页面
    pro_process= Field() #投资进度

class FinanceMapItem(Item):
    financeMap = Field()






