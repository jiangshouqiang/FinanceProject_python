from FinanceProject.db.mysql import Update,Query,Qry_Domin
from FinanceProject.log.FinanceLogger import FinanceLogger
INSERT_CONTENT = '''
INSERT INTO financeInfo(
DOMAIN ,organ,fin_name,pro_bate,begin_amt,
pro_cycle,pro_size,all_amt,can_amt,buy_button,buy_url,
pro_flag,from_url,process,cre_dt,cre_tm,cre_dm
) VALUES
(
%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,cre_dt(),cre_tm(),cre_dm()
)
'''
QRY_SCRAPY_SET = '''
SELECT
COLUMN_NAME,
COLUMN_RE,
COLUMN_DEF,
VAL_RE,
COLUMN_FLAG,
COL_MAP,
COL_MAP_VAL,
FUN_NAME,
JRN_ID
from SCRAPY_COLUMN_RE
WHERE COLUMN_STS='1'
AND
CONTENT_ID = %s
AND
now_dt() BETWEEN EFF_DT AND EXP_DT
'''

QRY_CLOUMN_SET = '''
SELECT
COLUMN_NAME,
COLUMN_RE,
COLUMN_DEF,
VAL_RE,
COLUMN_FLAG,
COL_MAP,
COL_MAP_VAL,
FUN_NAME,
JRN_ID
from SCRAPY_COLUMN_RE
WHERE COLUMN_STS='1'
AND
JRN_START_ID = %s
AND
now_dt() BETWEEN EFF_DT AND EXP_DT
'''
QRY_DOMIN = '''
SELECT
DOMIN_URL
FROM SCRAPY_DOMIN
WHERE DOMIN_STS='1'
AND now_dt() BETWEEN DOMIN_START_DT AND DOMIN_END_DT
'''

QRY_CONTENT = '''
SELECT
CONTENT_ID,
CONTENT_URL,
CONTENT_RE_URL,
CONTENT_RE_ISFOLLOW,
CONTENT_URL_FLAG,
CONTENT_HANDLE_FUND
FROM SCRAPY_CONTENT
WHERE CONTENT_STS='1'
AND now_dt() BETWEEN CONTENT_START_DT AND CONTENT_END_DT
'''

QRY_CONTENT_RE = '''
SELECT
CONTENT_ID,
CONTENT_URL,
CONTENT_RE_URL,
CONTENT_RE_ISFOLLOW,
CONTENT_URL_FLAG,
CONTENT_HANDLE_FUND
FROM SCRAPY_CONTENT
WHERE CONTENT_STS='1'
AND DOMIN_ID = %s
AND CONTENT_URL_FLAG = 'RE'
AND now_dt() BETWEEN CONTENT_START_DT AND CONTENT_END_DT
'''


@FinanceLogger()
def Scrapy_Update(val:[]):
    print("financeMap = ",val['financeMap'])
    for val_map in val['financeMap']:
        part_val = []
        part_val.append(get_val(val_map.get('domain','')))
        part_val.append(get_val(val_map.get('organ','')))
        part_val.append(get_val(val_map.get('fin_name','')))
        part_val.append(get_val(val_map.get('pro_bate','')))
        part_val.append(get_val(val_map.get('begin_amt','')))
        part_val.append(get_val(val_map.get('pro_cycle','')))
        part_val.append(get_val(val_map.get('pro_size','')))
        part_val.append(get_val(val_map.get('pro_all_amt','')))
        part_val.append(get_val(val_map.get('pro_can_amt','')))
        part_val.append(get_val(val_map.get('buy_button','')))
        part_val.append(get_val(val_map.get('buy_url','')))
        part_val.append(get_val(val_map.get('pro_flag','')))
        part_val.append(get_val(val_map.get('from_url','')))
        part_val.append(get_val(val_map.get('process','')))
        print('item = ',val_map.get('pro_cycle',''))
        Update(INSERT_CONTENT,part_val)
@FinanceLogger()
def Scrapy_Qry(val:[]):
    val = Query(QRY_SCRAPY_SET,val)
    return val
@FinanceLogger()
def Scrapy_sub_cloumn(val:[]):
    val = Query(QRY_CLOUMN_SET,val)
    return val

@FinanceLogger()
def Scrapy_content_re(val:[]):
    val = Query(QRY_CONTENT_RE,val)
    return val

@FinanceLogger()
def Domin_Qry():

    val = Query(QRY_DOMIN,[])
    domin = []
    for item in val:
        domin.append(item[0])
    print('domin=',domin)
    return domin
def Content_Qry():
    val = Query(QRY_CONTENT,[])
    obj = {}
    RE = []
    ST = []
    for item in val :
        if item[4] == 'RE':
            RE.append(item)
        elif item[4] == 'ST':
            ST.append(item)
    obj['RE'] = RE
    obj['ST'] = ST
    # print('content=',obj['RE'])
    return obj

def main_handle_Qry(val:[]):
    obj = {}
    val = Scrapy_Qry(val)
    RT = []
    CH = []
    I = []
    M = []
    for item in val :
        if item[4] == 'RT':
            RT.append(item)
        elif item[4] == 'CH':
            CH.append(item)
        elif item[4] == 'I':
            I.append(item)
        elif item[4] == 'M':
            M.append(item)
    obj['RT'] = RT
    obj['CH'] = CH
    obj['I'] = I
    obj['M'] = M
    RT_MAP = obj['M']
    # print(RT_MAP)
    return obj
# wacai_handle_Qry([1,])

# val = Scrapy_Qry([1,])
# print(Content_Qry())
# print(wacai_handle_Qry([2,]))
@FinanceLogger()
def get_val(val:[]):
    if not isinstance(val,list):
        val = [val,]
    if val is None  :
        return []
    if len(val) > 0 :
        return val[0]
    return ''

def load_scrapy():
    pass
