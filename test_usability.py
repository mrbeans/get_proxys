import requests,pdb
import save_to_redis
import threading
from concurrent.futures import ProcessPoolExecutor,as_completed

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
        print('********************************field********************************')
        return(False,'')

def run_test(url='http://www.baidu.com'):
    valid_proxys=[]
    proxys=save_to_redis.get_proxy()
    with ProcessPoolExecutor(500) as pool:
        results={pool.submit(exec_test,p,url):p for p in proxys.items()}
        for r in as_completed(results):
            if(r.result()[0]==True):
                valid_proxys.append(r.result()[1])
    return valid_proxys
