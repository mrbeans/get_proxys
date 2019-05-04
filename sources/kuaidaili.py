from splinter import Browser
import json,pdb

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer":"https://www.kuaidaili.com"
    }
tem_url="https://www.kuaidaili.com/free/inha/{0}/"
proxy_list=[]

class KuaiDaiLi(object):
    def run(self):
        for i in range(1,10):
            with Browser('chrome') as browser:
                url=tem_url.format(i)
                browser.visit(url)
                invalid=browser.find_by_text('Invalid Page')
                # pdb.set_trace()
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
                    # print('get new proxy : '+json.dumps(result))
            print('page {0} process down!'.format(i))
        return proxy_list
