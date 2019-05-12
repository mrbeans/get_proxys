#http://www.qydaili.com/free/?action=china&page=3
from splinter import Browser
import json,pdb

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer":"www.qydaili.com"
    }
tem_url="http://www.qydaili.com/free/?action=china&page={0}"
proxy_list=[]

class QYDaiLi(object):
    def run(self):
        for i in range(1,2):
            with Browser('chrome') as browser:
                browser.visit(tem_url.format(i))

                tr_list=browser.find_by_tag('tbody').first.find_by_tag('tr')
                if(tr_list==None or len(tr_list)<=0):
                    print('page {0} get 0 proxy,return'.format(i))
                    return
                print('page {0} get {1} proxys'.format(i,len(tr_list)))
                for tr in tr_list:
                    value_list=tr.value.split('\n')
                    # pdb.set_trace()
                    ip=value_list[1]
                    port=value_list[3]
                    protocal=value_list[7]
                    result={'ip':ip,'port':port,'protocal':protocal}
                    proxy_list.append(result)
                    print('get new proxy : '+json.dumps(result))
            print('page {0} process down!'.format(i))
        return proxy_list
