import requests,re,pdb
from bs4 import BeautifulSoup

ip_url='http://www.89ip.cn/tqdl.html?num=3000&address=&kill_address=&port=&kill_port=&isp='

class IP89(object):

    def __init__(self):
        Name='89ip'

    def run(self):
        response=requests.get(ip_url)
        if(response is None or response.content is None):
            return
        bs=BeautifulSoup(response.content,'lxml')
        ip_content=bs.select('div.layui-col-md8 div.fly-panel div')
        pattern = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.:\d{1,5}')
        all=pattern.findall(str(ip_content[0]))
        if(len(all)<=0):
            return
        proxy_list=[]
        for one in all:
            ip=one.split(':')[0]
            port=one.split(':')[1]
            protocal='http'
            result={'ip':ip,'port':port,'protocal':protocal}
            print(result)
            proxy_list.append(result)
        print(len(proxy_list))
        return proxy_list