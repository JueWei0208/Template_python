环境准备
需要python的环境
案例使用的是python版本2.7

需要Linux环境上有python的环境
以及有pip的python的安装命令
apt-get install python-pip

安装base64的python库
pip install pybase64

安装DES
安装命令
pip install pydes

#安装解密
pip install pyCrypto


Test_Case是测试用例 主要是发送http的请求和udp的请求 用于测试
目前使用的环境是ubuntu-18.04.4

用于接口的测试
只要执行
python main.py
就可以进相关接口的测试


修改Senddatahttp的中的Senddatahttp.py的IP和端口
修改Senddata的SendDatatoUDP.py的IP和端口
