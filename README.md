# 去中心化微博系统文档

## 系统设计架构：

![hyperledger-fabric架构 (/home/lhr/下载/flask运维管理系统.png)](/home/lhr/下载/hyperledger-fabric架构 (1).png)

针对去中心化环境下的微博系统设计，我在保持之前系统设计功能不变的情况下 ，将flask服务框架的底层数据持久切换为区块链，并通过共识机制保持节点间的一致性，在保持一致性的情况下，尽量保证高可用性，同时根据以太坊ERC20标准编写了一个简易代币，拥有奖励用户共同维护治理微博系统。

运行方法
1.安装Hyperledger fabric 1.1版本

2.

```
cd fabric-nodejs
./runApp.sh   #启动配置好的fabric集群，kafka/zookeeper/CA/order/peer
cd weibo
./channel.sh  #创建通道并加入通道
./install_weibo.sh #安装并实例化链码
./install_coin.sh #安装并实例化链码
```

`

成功后会看到以下界面：

![2020-05-17 12-43-48屏幕截图](/home/lhr/图片/微博/2020-05-17 12-43-48屏幕截图.png)

![2020-05-17 12-46-21屏幕截图](/home/lhr/图片/微博/2020-05-17 12-46-21屏幕截图.png)

3.运行微博系统

```
cd weibo 
export FLASK_MODE=default  #mac or linux
set FLASK_MODE=default     #windows
#本地运行
python manage.py runserver
#可以在http://127.0.0.1:5000/查看系统
#服务器上运行
python3 manage.py runserver --host='0.0.0.0' --port=8080
```

4.成功后结果如下 ：

![2020-05-17 12-55-39屏幕截图](/home/lhr/图片/微博/2020-05-17 12-55-39屏幕截图.png)