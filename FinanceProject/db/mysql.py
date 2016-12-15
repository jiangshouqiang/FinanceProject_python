from scrapy.conf import settings
from FinanceProject.log.FinanceLogger import FinanceLogger
import pymysql

user_name = settings['MYSQL_USER']
pwd       = settings['MYSQL_PWD']
DB        = settings['MYSQL_DB']
conn = pymysql.connect(user=user_name,password=pwd,database=DB,charset='UTF8')
cursor = conn.cursor()

# cursor.execute('select * from python')
# val = cursor.fetchall()
@FinanceLogger()
def Update(sql,val):
    cursor = conn.cursor()
    try:
        cursor.execute(sql,val)
        conn.commit()
    except:
        raise ConnectionError
        conn.rollback()
@FinanceLogger()
def Query(sql:str,val:[]):
    cursor = conn.cursor()
    try:
        cursor.execute(sql,val)
        val =  cursor.fetchall()
        print("val = ",val)
        return val
    except:
        raise ConnectionResetError
@FinanceLogger()
def Qry_Domin(sql:str):
    return Query(sql,[])

    # finally:
        # conn.close()
#
# SQL = 'INSERT INTO PYTHON (id) values (%s)'
# val = ['1','2']
# Update(SQL,val)