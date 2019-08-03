from splinter import Browser
import json,pdb
import sys
sys.path.append('..')
import setting

tem_url=["http://www.xiladaili.com/gaoni/{0}/","http://www.xiladaili.com/putong/{0}/"]
proxy_list=[]

class XiLaDaiLi(object):
    def __init__(self):
        Name='kuaidaili'

    def run(self):
        for url in tem_url:
            with Browser('chrome', headless=True) as browser:
                for i in range(1,setting.PAGE_SIZE):
                    if(i%setting.SLEEP_AFTER_PAGE==0):
                        sleep_sec=random.randint(3,8)
                        print('now sleep {sec} seconds'.format(sleep_sec))
                        time.sleep(sleep_sec)

                    url=url.format(i)
                    browser.visit(url)

                    tr_list=browser.find_by_tag('tbody').first.find_by_tag('tr')
                    if(tr_list==None or len(tr_list)<=0):
                        print('page {0} get 0 proxy,return'.format(i))
                        return
                    print('page {0} get {1} proxys'.format(i,len(tr_list)))
                    for tr in tr_list:
                        ip_port=tr.find_by_tag('td')[0].value
                        ip=ip_port.split(':')[0]
                        port=ip_port.split(':')[1]
                        protocal_value=tr.find_by_tag('td')[1].value
                        if('HTTP' in protocal_value):
                            protocal='HTTP'
                        if('HTTPS' in protocal_value):
                            protocal='HTTPS'
                        result={'ip':ip,'port':port,'protocal':protocal}
                        proxy_list.append(result)
                        print('get new proxy : '+json.dumps(result))
                print('page {0} process down!'.format(i))
        return proxy_list
