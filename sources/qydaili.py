from splinter import Browser
import json,pdb
import sys,time,random
sys.path.append('..')
import setting
from utils.BaseModel import BaseModel

tem_url="http://www.qydaili.com/free/?action=china&page={0}"
proxy_list=[]

class QYDaiLi(object):
    def __init__(self):
        self.Name='qiyundaili'

    def run(self):
        with Browser('chrome', headless=setting.USE_HEADLESS) as browser:
            for i in range(1,setting.PAGE_SIZE):
                browser.visit(tem_url.format(i))
                tr_list=browser.find_by_tag('tbody').first.find_by_tag('tr')
                if(tr_list==None or len(tr_list)<=0):
                    return
                for tr in tr_list:
                    value_list=tr.value.split('\n')
                    ip=value_list[1]
                    port=value_list[3]
                    protocal=value_list[7]
                    region=value_list[9]
                    proxy_list.append(BaseModel(ip,port,protocal,region).to_dict())
        return proxy_list
