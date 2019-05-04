import redis

r=redis.Redis(host='118.25.90.94',port=6379,db=2,password="tencent_redis")

def save_proxy(name,key,value):
    r.hset(name,key,value)

def get_proxy(key='proxys'):
    return r.hgetall(key)