#https://www.xicidaili.com/nn/
from splinter import Browser
import json,pdb

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer":"http://www.xicidaili.com"
    }
tem_url=["http://www.xicidaili.com/nn/{0}/","http://www.xicidaili.com/nt/{0}/"]
proxy_list=[]

class XiCiDaiLi(object):
    def run(self):
        for url in tem_url:
            for i in range(1,2):
                with Browser('chrome') as browser:
                    url=url.format(i)
                    browser.visit(url)

                    tr_list=browser.find_by_id('ip_list').first.find_by_tag('tr')
                    if(tr_list==None or len(tr_list)<=0):
                        print('page {0} get 0 proxy,return'.format(i))
                        return
                    print('page {0} get {1} proxys'.format(i,len(tr_list)-1))#因为第一行永远是标题th
                    for tr in tr_list:
                        # pdb.set_trace()
                        if(len(tr.find_by_tag('th'))>0):
                            continue
                        ip=tr.find_by_tag('td')[1].value
                        port=tr.find_by_tag('td')[2].value
                        protocal=tr.find_by_tag('td')[5].value
                        result={'ip':ip,'port':port,'protocal':protocal}
                        proxy_list.append(result)
                        print('get new proxy : '+json.dumps(result))
                print('page {0} process down!'.format(i))
        return proxy_list
