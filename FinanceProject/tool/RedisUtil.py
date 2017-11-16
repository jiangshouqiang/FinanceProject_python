from scrapy.conf import settings
import redis

host = settings['REDIS_HOST']
port = settings['REDIS_PORT']

r = redis.Redis(host= host,port= port)

def sadd(url:str):
    return r.sadd("url",url)

def delObj(key:str):
    return r.delete(key)

result = r.sadd('test1',1)
print(result)
result = r.sadd('test1',2)
print(result)
print(r.smembers('test1'))