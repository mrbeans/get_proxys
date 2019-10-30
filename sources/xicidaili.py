from splinter import Browser
import json,pdb
import sys,time,random
sys.path.append('..')
import setting
from utils.BaseModel import BaseModel

tem_url=["http://www.xicidaili.com/nn/{0}/","http://www.xicidaili.com/nt/{0}/"]
proxy_list=[]

class XiCiDaiLi(object):
    def __init__(self):
        self.Name='xicidaili'

    def run(self):
        for url in tem_url:
            with Browser('chrome', headless=setting.USE_HEADLESS) as browser:
                for i in range(1,setting.PAGE_SIZE):
                    url=url.format(i)
                    browser.visit(url)

                    tr_list=browser.find_by_id('ip_list').first.find_by_tag('tr')
                    if(tr_list==None or len(tr_list)<=0):
                        return proxy_list
                    for tr in tr_list:
                        if(len(tr.find_by_tag('th'))>0):
                            continue
                        ip=tr.find_by_tag('td')[1].value
                        port=tr.find_by_tag('td')[2].value
                        protocal=tr.find_by_tag('td')[5].value
                        region=tr.find_by_tag('td')[3].value
                        proxy_list.append(BaseModel(ip,port,protocal,region).to_dict())
        return proxy_list
