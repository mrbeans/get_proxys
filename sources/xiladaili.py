from splinter import Browser
import json,pdb,random,time
import sys
sys.path.append('..')
import setting
from utils.BaseModel import BaseModel

tem_url=["http://www.xiladaili.com/gaoni/{0}/","http://www.xiladaili.com/putong/{0}/"]
proxy_list=[]

class XiLaDaiLi(object):
    def __init__(self):
        self.Name='xiladaili'

    def run(self):
        for url in tem_url:
            with Browser('chrome', headless=setting.USE_HEADLESS) as browser:
                for i in range(1,setting.PAGE_SIZE):
                    url=url.format(i)
                    browser.visit(url)

                    tr_list=browser.find_by_tag('tbody').first.find_by_tag('tr')
                    if(tr_list==None or len(tr_list)<=0):
                        return proxy_list
                    for tr in tr_list:
                        ip_port=tr.find_by_tag('td')[0].value
                        ip=ip_port.split(':')[0]
                        port=ip_port.split(':')[1]
                        protocal_value=tr.find_by_tag('td')[1].value
                        if('HTTP' in protocal_value):
                            protocal='HTTP'
                        if('HTTPS' in protocal_value):
                            protocal='HTTPS'
                        region=tr.find_by_tag('td')[3].value
                        proxy_list.append(BaseModel(ip,port,protocal,region).to_dict())
        return proxy_list
