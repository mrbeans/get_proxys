from splinter import Browser
import json,pdb
import sys,time,random
sys.path.append('..')
import setting
from utils.BaseModel import BaseModel

tem_url="https://www.kuaidaili.com/free/inha/{0}/"
proxy_list=[]

class KuaiDaiLi(object):
    def __init__(self):
        self.Name='kuaidaili'

    def run(self):
        with Browser('chrome', headless=setting.USE_HEADLESS) as browser:
            for i in range(1,setting.PAGE_SIZE):
                url=tem_url.format(i)
                browser.visit(url)
                if(len(browser.title)<=0):
                    return proxy_list
                tr_list=browser.find_by_id('list').first.find_by_tag('tbody').first.find_by_tag('tr')
                if(tr_list==None or len(tr_list)<=0):
                    return proxy_list
                for tr in tr_list:
                    ip=tr.find_by_tag('td')[0].value
                    port=tr.find_by_tag('td')[1].value
                    protocal=tr.find_by_tag('td')[3].value
                    region=tr.find_by_tag('td')[4].value
                    proxy_list.append(BaseModel(ip,port,protocal,region).to_dict())
        return proxy_list
