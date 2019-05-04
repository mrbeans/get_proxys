import requests,pdb
import save_to_redis
import threading
from concurrent.futures import ProcessPoolExecutor

def exec_test(p,url):
    proxy=eval(p[1].decode('utf-8'))
    proxies={
        'http':'http://{0}:{1}'.format(proxy['ip'],proxy['port'])
    }
    if(proxy['protocal'].lower()=='https'):
        proxies={
            'https':'https://{0}:{1}'.format(proxy['ip'],proxy['port'])
        }
    try:
        requests.get(url,proxies=proxies,timeout=5)
        print('--------------------------------success--------------------------------')
        return (True,proxy)
    except requests.exceptions.RequestException as ex:
        print(ex)
        return(False,'')

def run_test(url='http://www.baidu.com'):
    valid_proxys=[]
    proxys=save_to_redis.get_proxy()
    with ProcessPoolExecutor(50) as pool:
        for p in proxys.items():
            result=exec_test(p,url)
            if(result[0]==True):
                valid_proxys.append(result[1])
    return valid_proxys
