from sources import kuaidaili,xiladaili,xicidaili,qydaili,ip89,ip66
import save_to_redis,test_usability
import sys,json,shortuuid,pdb

def get():
    spiders=[kuaidaili.KuaiDaiLi(),xiladaili.XiLaDaiLi(),xicidaili.XiCiDaiLi(),qydaili.QYDaiLi(),ip89.IP89()]
    for spider in spiders:
        try:
            proxys=spider.run()
            print('get {0} proxys from {1} done'.format(len(proxys),spider.Name))
            save_to_redis.save_proxy('proxys',spider.Name,json.dumps(proxys))
        except Exception as ex:
            print('error------'+str(ex))

#todo 有时候由于网络或者其他原因，一次性检查的数据量多，太耗时，建议检查一个，存进去一个。这样可以边检查边使用
def check():
    valid_proxys=test_usability.run_test()
    for vproxy in valid_proxys:
        save_to_redis.save_proxy('valid_proxy',shortuuid.uuid(),json.dumps(vproxy))

if __name__=='__main__':
    args=sys.argv
    if(len(args)<2 or args[1]=='get'):
        get()
        print('get proxy done')
        check()
        print('check all proxy done')
        print('all process done')
    elif(args[1]=='check'):
        check()
        print('check all proxy done')
    else:
        print('invalid command')
