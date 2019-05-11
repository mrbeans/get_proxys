from sources import kuaidaili
from sources import xiladaili
import save_to_redis,test_usability
import sys,json,shortuuid

#chromedriver各版本下载地址 http://chromedriver.storage.googleapis.com/index.html
if __name__=='__main__':
    args=sys.argv
    if(len(args)<2):
        print('请输入参数')
    elif(args[1]=='get'):
        # spider=kuaidaili.KuaiDaiLi()
        spider=xiladaili.XiLaDaiLi()
        proxys=spider.run()
        for proxy in proxys:
            save_to_redis.save_proxy('proxys',shortuuid.uuid(),json.dumps(proxy))
        print('get proxys done')
    elif(args[1]=='check'):
        valid_proxys=test_usability.run_test()
        for vproxy in valid_proxys:
            save_to_redis.save_proxy('valid_proxy',shortuuid.uuid(),json.dumps(vproxy))
