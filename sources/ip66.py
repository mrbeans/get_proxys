#http://www.66ip.cn/mo.php?sxb=&tqsl=100000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=
#http://www.66ip.cn/nmtq.php?getnum=10000&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip

import requests,pdb,re
from bs4 import BeautifulSoup
import sys
sys.path.append('..')
from utils.BaseModel import BaseModel

urls = ['http://www.66ip.cn/mo.php?sxb=&tqsl=100000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=',
'http://www.66ip.cn/nmtq.php?getnum=10000&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip']
proxy_list=[]

class IP66(object):
    def __init__(self):
        self.Name='ip66'

    def run(self):
        for url in urls:
            response = requests.get(url)
            if(response.status_code != 200 or response.content is None):
                continue
            bs=BeautifulSoup(response.content,'lxml')
            pattern = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}.:\d{1,5}')
            all=pattern.findall(str(bs.text))
            for ip_port in all:
                ip=ip_port.split(':')[0]
                port=int(ip_port.split(':')[1])
                proxy_list.append(BaseModel(ip,port,'http','中国').to_dict())
        return proxy_list