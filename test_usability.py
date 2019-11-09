import requests,pdb,sys,json,shortuuid
import save_to_redis
import threading
from concurrent.futures import ProcessPoolExecutor,as_completed

def exec_test(proxy,url):
    proxies={
        'http':'http://{0}:{1}'.format(proxy['ip'],proxy['port'])
    }
    if(proxy['protocal'].lower()=='https'):
        proxies={
            'https':'https://{0}:{1}'.format(proxy['ip'],proxy['port'])
        }
    try:
        requests.get(url,proxies=proxies,timeout=5)
        #print('--------------------------------success--------------------------------')
        return (True,proxy)
    except requests.exceptions.RequestException as ex:
        # print('********************************field********************************')
        return(False,'')

def run_test(url='http://www.baidu.com'):
    valid_proxys=[]
    proxys=save_to_redis.get_proxy()
    worker_count= 500
    if(sys.platform=='win32'):
        worker_count=60
    for key,ips in proxys.items():
        proxy_list=json.loads(ips.decode('utf-8'))
        with ProcessPoolExecutor(worker_count) as pool:
            results={pool.submit(exec_test,p,url):p for p in proxy_list}
            for r in as_completed(results):
                if(r.result()[0]==True):
                    valid_proxys.append(r.result()[1])
    return valid_proxys
