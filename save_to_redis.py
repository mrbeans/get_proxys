import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=5)

def save_proxy(name,key,value):
    r.hset(name,key,value)

def get_proxy(key='proxys'):
    return r.hgetall(key)