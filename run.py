from sources import kuaidaili,xiladaili,xicidaili,qydaili
import save_to_redis,test_usability
import sys,json,shortuuid

#chromedriver各版本下载地址 http://chromedriver.storage.googleapis.com/index.html
if __name__=='__main__':
    args=sys.argv
    if(len(args)<2):
        print('请输入参数')
    elif(args[1]=='get'):
        spiders=[kuaidaili.KuaiDaiLi(),xiladaili.XiLaDaiLi(),xicidaili.XiCiDaiLi(),qydaili.QYDaiLi()]
        for spider in spiders:
            try:
                proxys=spider.run()
                for proxy in proxys:
                    save_to_redis.save_proxy('proxys',shortuuid.uuid(),json.dumps(proxy))
                print('get proxys from {0} done'.format(spider.Name))
            except Exception as ex:
                print(ex)
        print('all process done')
    elif(args[1]=='check'):
        valid_proxys=test_usability.run_test()
        for vproxy in valid_proxys:
            save_to_redis.save_proxy('valid_proxy',shortuuid.uuid(),json.dumps(vproxy))
