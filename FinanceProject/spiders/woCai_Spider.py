from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from FinanceProject.items import FinanceprojectItem,FinanceMapItem
from FinanceProject.log.FinanceLogger import FinanceLogger
from scrapy.conf import settings
from FinanceProject.db.dao.ScrapyDao import wacai_handle_Qry,Content_Qry,Domin_Qry
import re


#挖财网数据抓取
@FinanceLogger()
def handle_wacai_response(response):
    itemMap = FinanceMapItem()
    # self.logger.info(response.url)
    financeMap = []
    i = 0
    for items in response.xpath("//li[@class='fundItem sellList']"):
        item = FinanceprojectItem()
        # self.logger.info(items.extract())
        item['pro_flag'] = items.xpath("span[@class='newUserTag']/text()").extract()
        item['from_url'] = [response.url,]
        item['domain']   = [re.search(r'([http:\/\/|https:\/\/].*\.\w+)',response.url).group(1),]
        item['organ']    = ['wacai',]
        item['fin_name'] = items.xpath("h4/a/text()").extract()
        # bate = items.xpath('div//div[@class="listDetail"]/em/text()')[1].re(r'(\d+\.\d+\%).+~.+(\d+\.\d+\%)')
        bate = items.xpath('div//div[@class="listDetail indexRow"]/em/text()')
        if bate is not None:
            val = bate.re(r'(\d+\.\d+\%)')
            # self.logger.info(val)
            if val is not None and len(val) == 2:
                item['pro_bate'] = [val[0] + '~' + val[1],]
            else:
                item['pro_bate'] = items.xpath('div//div[@class="listDetail"]/em/text()')[1].re(r'(\d+\.\d+\%)')
        else:
            item['pro_bate'] = items.xpath('div//div[@class="listDetail"]/em/text()')[1].re(r'(\d+\.\d+\%)')
        for part in items.xpath('div//div[@class="listDetail"]'):
            obj_val = part.xpath('em/text()')
            label_name = obj_val[0].extract()
            if label_name.find('已购人数') > -1 :
                item['pro_size'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            if label_name.find('投资总额') > -1 :
                item['pro_all_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            if label_name.find('起购金额') > -1 :
                item['begin_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            if label_name.find('投资期限') > -1 :
                item['pro_cycle'] = obj_val[1].re(r'\D*(\d{1,8}\w)')
            if label_name.find('投资进度') > -1 :
                item['pro_process'] = part.xpath('em/i/text()').re(r'\D*(\d+)')
            if label_name.find('剩余金额') > -1 :
                item['pro_can_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
        # item['begin_amt']= items.xpath('div//div[@class="listDetail"]/em/text()')[5].extract()
        # item['pro_cycle']= items.xpath('div//div[@class="listDetail"]/em/text()')[7].re(r'\D*(\d{1,4}\.?\d{1,3}\w)')
        # item['pro_size'] = items.xpath('div//div[@class="listDetail"]/em/text()')[3].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
        item['buy_button']= items.xpath('div//div[@class="column col-2 tr"]/a/text()').extract()
        item['buy_url']  = items.xpath('div//div[@class="column col-2 tr"]/a/@href').extract()
        financeMap.append(item)
        # self.logger.info(dir(itemMap))
    itemMap['financeMap'] = financeMap
    # print(itemMap)
    yield itemMap
@FinanceLogger()
def handle_wacai(response):
    itemMap = FinanceMapItem()
    financeMap = []
    wacai_obj = {}
    if wacai_obj is None or len(wacai_obj) == 0 :
        wacai_obj = wacai_handle_Qry([1,])
    RT_MAP = wacai_obj['RT']
    I_MAP  = wacai_obj['I']
    M_MAP  = wacai_obj['M']
    CH_MAP  = wacai_obj['CH']

    for I in I_MAP:
        if I[0] == 'pro_flag':
            pro_flag_xp = I[1]
        elif I[0] == 'domain':
            domain_re = I[3]
        elif I[0] == 'organ':
            organ = I[2]
        elif I[0] == 'fin_name':
            fin_name_xp = I[1]
        elif I[0] == 'pro_bate':
            pro_bate_xp = I[1]
            pro_bate_re = I[3]
        elif I[0] == 'buy_button':
            buy_button_xp = I[1]
        elif I[0] == 'buy_url':
            buy_url_xp = I[1]
    for CH in CH_MAP :
        if CH[0] == 'pro_bate':
            pro_bate_ch_xp1 = CH[1]
            pro_bate_ch_re = CH[3]
        elif CH[0] == 'map':
            map_ch_xp1 = CH[1]
            map_ch_xp2 = CH[3]
    for items in response.xpath(RT_MAP[0][1]):
        item = FinanceprojectItem()
        # self.logger.info(items.extract())

        item['pro_flag'] = items.xpath(pro_flag_xp).extract()
        item['from_url'] = [response.url,]
        domain_complie = re.compile(domain_re)
        item['domain']   = [domain_complie.search(response.url).group(1),]
        item['organ']    = [organ,]
        item['fin_name'] = items.xpath(fin_name_xp).extract()
        # bate = items.xpath('div//div[@class="listDetail"]/em/text()')[1].re(r'(\d+\.\d+\%).+~.+(\d+\.\d+\%)')
        bate = items.xpath(pro_bate_ch_xp1)
        if bate is not None:
            val = bate.re(r''+pro_bate_ch_re)
            # bate_compile = re.compile(pro_bate_ch_re)
            # val = bate_compile.search(bate)
            # self.logger.info(val)
            if val is not None and len(val) == 2:
                item['pro_bate'] = [val[0] + '~' + val[1],]
            else:
                item['pro_bate'] = items.xpath(pro_bate_xp)[1].re(r''+pro_bate_re)
        else:
            item['pro_bate'] = items.xpath(pro_bate_xp)[1].re(r''+pro_bate_re)
        for part in items.xpath(map_ch_xp1):
            obj_val = part.xpath(map_ch_xp2)
            label_name = obj_val[0].extract()
            for M in M_MAP :
                if label_name.find(M[6]) > -1:
                    item[M[0]] = obj_val[1].re(r''+M[3])
            # if label_name.find('已购人数') > -1 :
            #     item['pro_size'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            # if label_name.find('投资总额') > -1 :
            #     item['pro_all_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            # if label_name.find('起购金额') > -1 :
            #     item['begin_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
            # if label_name.find('投资期限') > -1 :
            #     item['pro_cycle'] = obj_val[1].re(r'\D*(\d{1,8}\w)')
            # if label_name.find('投资进度') > -1 :
            #     item['pro_process'] = part.xpath('em/i/text()').re(r'\D*(\d+)')
            # if label_name.find('剩余金额') > -1 :
            #     item['pro_can_amt'] = obj_val[1].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
        # item['begin_amt']= items.xpath('div//div[@class="listDetail"]/em/text()')[5].extract()
        # item['pro_cycle']= items.xpath('div//div[@class="listDetail"]/em/text()')[7].re(r'\D*(\d{1,4}\.?\d{1,3}\w)')
        # item['pro_size'] = items.xpath('div//div[@class="listDetail"]/em/text()')[3].re(r'\D*(\d{1,8}\.?\d{1,3}\w)')
        item['buy_button']= items.xpath(buy_button_xp).extract()
        item['buy_url']  = items.xpath(buy_url_xp).extract()
        financeMap.append(item)
        # self.logger.info(dir(itemMap))
    itemMap['financeMap'] = financeMap
    # print(itemMap)
    yield itemMap

class woCai_spider(CrawlSpider):
    name = "wenying"
    allowed_domains = Domin_Qry()
    # print('domin=',allowed_domains)
    # allowed_domains.append('www.xiaoniu88.com');
    start_urls = []
    for item in Content_Qry()['ST']:
        start_urls.append(item[1])
    # print('start_urls=',start_urls)
    # start_urls.append('http://www.xiaoniu88.com/product/investment');
    rules = []
    for rule in Content_Qry()['RE']:
        rules.append(Rule(LinkExtractor(allow=(rule[2])),rule[5],follow=rule[3]))
        # print('rules=',rule[2],rule[5],rule[3])
    # rules.append(Rule(LinkExtractor(allow='http://www.xiaoniu88.com/product/investment'),"parse_item",follow=True,));
    # rules.append(Rule(LinkExtractor(allow='http://www.xiaoniu88.com/product/investment[/\d+]?$'),"parse_item",follow=True,));
    # start_urls = ["http://8.wacai.com/list/wenying","http://www.xiaoniu88.com/product/investment"]
    # rules = [
    #     Rule(LinkExtractor(allow=("http://8.wacai.com/list/wenying/p1",)),'parse_item',follow=True,),
    #     Rule(LinkExtractor(allow='http://8.wacai.com/list/wenying/p\d+$'),"parse_item",follow=True,),
     #    Rule(LinkExtractor(allow='http://www.xiaoniu88.com/product/investment'),"parse_item",follow=True,),
    #     # Rule(LinkExtractor(allow='http://www.xiaoniu88.com/product/investment[/\d+]?$'),"parse_item",follow=True,),
    # ]
    # rules = [
    #     Rule(SgmlLinkExtractor(allow=(r'/list/wenying/p\d+$'),restrict_xpaths=(r"//li[@class='fundItem sellList']")),callback='parse_item',follow=True),
    # ]
    # @FinanceLogger()
    def parse_item(self,response):
        self.logger.info(response)
        return handle_wacai(response)
    @FinanceLogger()
    def xiaoniu_item(self,response):
        itemMap = FinanceMapItem()
        # self.logger.info(response.url)
        financeMap = []
        xiaoniu_obj = {}
        if xiaoniu_obj is None or len(xiaoniu_obj) == 0 :
            xiaoniu_obj = wacai_handle_Qry([2,])
        RT_MAP = xiaoniu_obj['RT']
        I_MAP  = xiaoniu_obj['I']
        for items in response.xpath(RT_MAP[0][1]):
            # print('items====',items.xpath("li/h1/div/text()").extract())
            item = FinanceprojectItem()
            item['from_url'] = [response.url,]
            for part in I_MAP:
                if part[0] == 'domain':
                    domain_complie = re.compile(part[3])
                    item['domain'] = [domain_complie.search(response.url).group(1),]
                elif part[0] == 'organ':
                    item['organ'] = [part[2],]
                elif part[3] is not None and part[3] != '':
                    # objs=items.xpath(part[1]).extract()
                    # print('objs===',items.xpath(part[1]).extract())
                    # if len(objs) != 0:
                    item[part[0]] = items.xpath(part[1]).re(r''+part[3])
                    # print('part=',part[3])
                else:
                    item[part[0]] = items.xpath(part[1]).extract()
            financeMap.append(item)
        itemMap['financeMap'] = financeMap
        yield itemMap
    @FinanceLogger()
    def wukong_item(self,response):
        itemMap = FinanceMapItem()
        # self.logger.info(response.url)
        financeMap = []
        xiaoniu_obj = {}
        if xiaoniu_obj is None or len(xiaoniu_obj) == 0 :
            xiaoniu_obj = wacai_handle_Qry([3,])
        RT_MAP = xiaoniu_obj['RT']
        I_MAP  = xiaoniu_obj['I']
        for items in response.xpath(RT_MAP[0][1]):
            # print('items====',items.xpath("li/h1/div/text()").extract())
            item = FinanceprojectItem()
            item['from_url'] = [response.url,]
            for part in I_MAP:
                if part[0] == 'domain':
                    domain_complie = re.compile(part[3])
                    item['domain'] = [domain_complie.search(response.url).group(1),]
                elif part[0] == 'organ':
                    item['organ'] = [part[2],]
                elif part[0] == 'pro_cycle' or part[0] == 'pro_can_amt':
                    item[part[0]] = [''.join(items.xpath(part[1]).re(r''+part[3])).replace('</b>',''),];
                elif part[3] is not None and part[3] != '':
                    # objs=items.xpath(part[1]).extract()
                    # print('objs===',items.xpath(part[1]).extract())
                    # if len(objs) != 0:
                    item[part[0]] = items.xpath(part[1]).re(r''+part[3])
                    # print('part=',part[3])
                else:
                    item[part[0]] = items.xpath(part[1]).extract()
            financeMap.append(item)
        itemMap['financeMap'] = financeMap
        yield itemMap

from scrapy.crawler import CrawlerProcess
if __name__ == "__main__":
    process = CrawlerProcess(settings)
    spiders = woCai_spider()
    process.crawl(spiders)
    process.start()


