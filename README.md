<p align="center">
    <img width="100" src="https://project-icons.oss-cn-shanghai.aliyuncs.com/p.png" alt="Proxys logo">
</p>
<h2 align="center">给你的爬虫添加免费代理</h2>
<hr />

### get_proxys是一个可以自动获取一批免费且可用的ip的程序

#### 严正声明：
* 此程序制作之初以学习为目的，请勿使用本程序对ip来源网站或其他网站造成正常使用压力
* 如果因为此程序对您的网站造成了影响或其他破坏性的问题，可以随时联系我修改或关闭此程序，邮箱地址：<justnull@126.com>

获取的ip来自网络开放信息，所以ip可能随时会失效，建议您在使用的时候做好异常处理，比如每次需要的时候都获取一次、设置合理的超时等。获取到的ip包含了http和https的类型

程序设计思路：使用splinter遍历获取“快代理”、“西刺代理”、“西拉代理”、“旗云代理”公布的免费代理列表，并存入redis，程序跑完之后，会使用获取到的ip作为代理访问“百度”来验证可用性，并将结果存入redis。

> PS:测试过程中，共获取了325条IP，其中验证通过的有182条，可用率56%

<hr />

#### 使用方法：
> 获取IP（获取结束后会自动进行检查）
```
> git clone https://github.com/mrbeans/get_proxys.git
> cd get_proxys
> pip install -r requirements.txt
> python run.py
```
> 检查IP可用性
```
> python run.py check
```

#### 运行截图：
* 获取过程
![获取过程](https://project-imgs.oss-cn-shanghai.aliyuncs.com/%E8%BE%93%E5%87%BA2.png)
* 检查过程
![检查过程](https://project-imgs.oss-cn-shanghai.aliyuncs.com/check2.png)

#### 数据存储结构：
![redis存储结构](https://project-imgs.oss-cn-shanghai.aliyuncs.com/proxys.png)

#### 其他说明：
* 每个网站的免费代理，每获取10页数据之后会随机休眠3-8s以降低对来源网站的压力
* 数据存储在redis中的第6个[索引为5]数据库中，全量的ip key为“proxys”，筛选过后的ip key为“valid_proxy”
* 如果redis需要验证，请在save_to_redis中的连接对象中配置password参数
* 程序运行必须的插件chromedriver各版本下载地址 http://chromedriver.storage.googleapis.com/index.html

#### TODO:
* 将程序改成服务，支持7*24h运行，每隔一定的时间间隔自动检测可用的IP，如果可用IP下降到片一定的阈值内，则自动获取新的ip代理列表
* 添加更多来源
