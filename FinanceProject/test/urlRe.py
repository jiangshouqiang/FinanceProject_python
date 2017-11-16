import re

url = "https://m.wukonglicai.com/weixin/specialSale/index.html"
domin= "m.wukonglicai.comx"

obj = url.find(domin)
print(obj)

value =  {'productName': '新手专享', 'maxProfit': '', 'createTime': None, 'restAmount': '38448163.00', 'productPackageCode': 'WKBTM02117051801', 'mdesc': None, 'yields': '12.0', 'url': None, 'totalAmount': None, 'activityInfo': '', 'hdesc': None, 'startTime': None, 'productType': 'T', 'isShowGreen': None, 'upProfit': '', 'accountSign': None, 'timeLong': '21', 'productCode': 'TFB-20170412', 'isShowActivityInfo': 'F', 'endTime': None, 'extraProfit': 'F', 'maxInvest': 50000.0, 'isShowextraInfo': 'F', 'minInvest': 100.0, 'baseYields': '12.0', 'isUser': 'F', 'startDateAPP': None, 'startTimeAPP': None, 'extraInfo': '', 'isShow': 'T'}
print(value["baseYields"])

haveUrl = ['https://8.wacai.com/finance/web/list',]
print(haveUrl.count("https://8.wacai.com/finance/web/list?pageId=401&pageNo=3"))