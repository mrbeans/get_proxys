from splinter import Browser
import json,pdb

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Referer":"http://www.xiladaili.com"
    }
tem_url=["http://www.xiladaili.com/gaoni/{0}/","http://www.xiladaili.com/putong/{0}/"]
proxy_list=[]

class XiLaDaiLi(object):
    def run(self):
        for url in tem_url:
            for i in range(1,10):
                with Browser('chrome') as browser:
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
