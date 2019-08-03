from splinter import Browser
import json,pdb
import sys,time,random
sys.path.append('..')
import setting

tem_url="https://www.kuaidaili.com/free/inha/{0}/"
proxy_list=[]

class KuaiDaiLi(object):
    def __init__(self):
        Name='kuaidaili'

    def run(self):
        with Browser('chrome', headless=True) as browser:
            for i in range(1,setting.PAGE_SIZE):
                if(i%setting.SLEEP_AFTER_PAGE==0):
                        sleep_sec=random.randint(3,8)
                        print('now sleep {sec} seconds'.format(sleep_sec))
                        time.sleep(sleep_sec)
                url=tem_url.format(i)
                browser.visit(url)
                invalid=browser.find_by_text('Invalid Page')
                if(len(browser.title)<=0):
                    print('Invalid Page,return')
                    return
                tr_list=browser.find_by_id('list').first.find_by_tag('tbody').first.find_by_tag('tr')
                if(tr_list==None or len(tr_list)<=0):
                    print('page {0} get 0 proxy,return'.format(i))
                    return
                print('page {0} get {1} proxys'.format(i,len(tr_list)))
                for tr in tr_list:
                    ip=tr.find_by_tag('td')[0]
                    port=tr.find_by_tag('td')[1]
                    protocal=tr.find_by_tag('td')[3]
                    result={'ip':ip.value,'port':port.value,'protocal':protocal.value}
                    proxy_list.append(result)
                    print('get new proxy : '+json.dumps(result))
            print('page {0} process down!'.format(i))
        return proxy_list
