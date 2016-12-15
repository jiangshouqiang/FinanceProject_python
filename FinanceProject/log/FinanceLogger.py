from scrapy.conf import settings
from functools import wraps
import logging
import logging.handlers
import datetime
import os
import inspect
import imp

now = datetime.datetime.now()
def get_variable():
    for va in inspect.stack() :
        for v in va:
            if inspect.isframe(v):
                print("v == ",v.f_locals)

def FinanceLogger(name=None):
    '''
    该模块用于打印使用该注释函数的日志信息
    :param level:
    :param name:
    :param message:
    :return:
    '''
    def decorate(func):
        logFileName = name if name else func.__code__.co_filename.split('/')[-1:][0].split(".")[0]
        # print(dir(func))
        # print(func.__name__)
        # print(dir(func.__code__))
        # print(func.__code__.co_filename.split('/')[-1:][0].split(".")[0])
        level=settings.get("LOG_LEVEL")
        logFileDir = settings.get("LOG_FILE_DIR")
        log = logging.getLogger(logFileName)
        log.setLevel(level)
        if(not os.path.exists(logFileDir+now.strftime('%Y%m%d')+"/")):
            os.makedirs(logFileDir+now.strftime('%Y%m%d')+"/")
        func_name = func.__name__
        handler = logging.handlers.RotatingFileHandler(logFileDir+now.strftime('%Y%m%d')+"/"+logFileName+".log",maxBytes=1024*1024,backupCount=5)
        handler.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelno)s - '+func_name+' - %(message)s')
        ch.setFormatter(formatter)
        handler.setFormatter(formatter)
        log.addHandler(handler)
        log.addHandler(ch)
        logMessage = ""
        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logFileName)
            logMessage = str(args)
            # print("----",logMessage)
            log.info(logMessage)
            value = func(*args,**kwargs)
            get_variable()
            # setattr(func,"get_variable",get_variable())
            return value
        return wrapper

    return decorate

# import sys
# @FinanceLogger()
# def add(x:int,y:int):
#     # print(sys._getframe().f_code.co_name)
#     w=20
#     # get_variable()
#     return x+y
# add(2,3)

