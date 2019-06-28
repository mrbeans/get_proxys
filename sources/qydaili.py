#http://www.qydaili.com/free/?action=china&page=3
from splinter import Browser
import json,pdb
import sys,time,random
sys.path.append('..')
import setting

tem_url="http://www.qydaili.com/free/?action=china&page={0}"
proxy_list=[]

class QYDaiLi(object):
    def __init__(self):
        Name='kuaidaili'

    def run(self):
        with Browser('chrome') as browser:
            for i in range(1,setting.PAGE_SIZE):
                if(i%setting.SLEEP_AFTER_PAGE==0):
                        sleep_sec=random.randint(3,8)
                        print('now sleep {sec} seconds'.format(sleep_sec))
                        time.sleep(sleep_sec)

                browser.visit(tem_url.format(i))

                tr_list=browser.find_by_tag('tbody').first.find_by_tag('tr')
                if(tr_list==None or len(tr_list)<=0):
                    print('page {0} get 0 proxy,return'.format(i))
                    return
                print('page {0} get {1} proxys'.format(i,len(tr_list)))
                for tr in tr_list:
                    value_list=tr.value.split('\n')
                    ip=value_list[1]
                    port=value_list[3]
                    protocal=value_list[7]
                    result={'ip':ip,'port':port,'protocal':protocal}
                    proxy_list.append(result)
                    print('get new proxy : '+json.dumps(result))
            print('page {0} process down!'.format(i))
        return proxy_list
