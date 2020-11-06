#!/usr/bin/python
# -*- coding=utf-8-*-
import socket
import sys
import re
import json
#加入文件的路径
sys.path.append('./Parsing')
#sys.path.append('../Parsing')
#from 后面跟文件的名字 import 后面是类的名字
from Parsing import DESUtil

#UDPIP="192.167.111.1"
UDPIP="127.0.0.1"
UDPport=9999
Key="12345678"
Linux_mac="3333"
#发送数据到UDP服务器
#返回服务器接收的数据
def Senddata(data):
    paring =DESUtil()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address=(UDPIP,UDPport)
    #先将数据加密
    senddata=paring.encryt(data,Key)
    #print ("data:%s"%(senddata))
    #发送数据
    client_socket.sendto(senddata.encode(),server_address)
    #然后接收客户端的数据
    receive_data, sender_address = client_socket.recvfrom(1024)
    #然后将接收到的数据解密
    return paring.decrypt(receive_data,Key)

#人脸设备向安全设备发送绑定
def Senddata1():
    #组装json的数据
    data= {\
    "Code":"1",\
    "Timestamp":"20200826095157",\
    "Data":{\
    "Linux_mac":Linux_mac,\
    "Linux_version":"1.0",\
    "Driver_list":\
    [\
    {"Drivername":"driver1","Driveversion":"1.0"},\
    {"Drivername":"driver2","Driveversion":"2.0"}\
    ],\
    "Process_list":\
    [
    {"Processname":"process1","Processversion":"1.0"},\
    {"Processname":"process2","Processversion":"2.1"}\
    ],\
    "Start_time":"202002",\
    "End_time":"202020"\
    }\
    }
    #将数据转为json数据
    datajson = json.dumps(data)
    #发送数据给udp服务器
    return Senddata(datajson)

#设备验证
def Senddata2():
    #组装json的数据
    data= {\
    "Code":"2",\
    "Timestamp":"20200826095157",\
    "Data":{\
    "Linux_mac":Linux_mac,\
    "Linux_version":"1.0",\
    "Driver_list":\
    [\
    {"Drivername":"driver1","Driveversion":"1.0"},\
    {"Drivername":"driver2","Driveversion":"2.0"}\
    ],\
    "Process_list":\
    [
    {"Processname":"process1","Processversion":"1.0"},\
    {"Processname":"process2","Processversion":"2.1"}\
    ],\
    "Start_time":"202002",\
    "End_time":"202020"\
    }\
    }
    #将数据转为json数据
    datajson = json.dumps(data)
    #发送数据给udp服务器
    return Senddata(datajson)

#向安全设备上报人脸设备的状态
#1代表外网状态是正常的
def Senddata3():
    #组装json的数据 
    data= {\
    "Code":"3",\
    "Timestamp":"20200826095157",\
    "Data":{\
    "Linux_mac":Linux_mac,\
    "Outer_netstatus":"1"}\
    }
    #将数据转为json数据
    datajson = json.dumps(data)
    #发送数据给udp服务器
    return Senddata(datajson)

#向安全设备上报人脸设备心跳 以此来判断设备是否在线
def Senddata4():
    #组装json的数据
    data= {\
    "Code":"4",\
    "Timestamp":"20200826095157",\
    "Data":{\
    "Linux_mac":Linux_mac,\
    }\
    }
    #将数据转为json数据
    datajson = json.dumps(data)
    #发送数据给udp服务器
    return Senddata(datajson)

#向安全设备上报自己的ip bcos的groupid 以及mac地址
Cacrt="-----BEGIN CERTIFICATE-----MIIBvjCCAWSgAwIBAgIUCf3eT4A7qEMqf7zpE2bNfIUdJAQwCgYIKoZIzj0EAwIwNTEOMAwGA1UEAwwFY2hhaW4xEzARBgNVBAoMCmZpc2NvLWJjb3MxDjAMBgNVBAsMBWNoYWluMCAXDTIwMTEwMzA2NTgyN1oYDzIxMjAxMDEwMDY1ODI3WjA1MQ4wDAYDVQQDDAVjaGFpbjETMBEGA1UECgwKZmlzY28tYmNvczEOMAwGA1UECwwFY2hhaW4wVjAQBgcqhkjOPQIBBgUrgQQACgNCAAQGGZCe8MKPCvWH8CiiQHqefEth8p2Zm+XUFQWyd5NItMm4muyrrIbVcfsxU42p9fowUg5gOhL6HbOHixCeu7bUo1MwUTAdBgNVHQ4EFgQUfMKZqsmwJ08BvgtTwPx+FOwKXTwwHwYDVR0jBBgwFoAUfMKZqsmwJ08BvgtTwPx+FOwKXTwwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAyX1YSJ+bw8YJGxARNYlSPPcGojFkab1yhPGCB58bfKsCIDaMaWMAtcBQfup1gqqHvHmMHGhbJVYNs/6+XxHDEhsC-----END CERTIFICATE-----"
Nodekey="-----BEGIN PRIVATE KEY-----MIGEAgEAMBAGByqGSM49AgEGBSuBBAAKBG0wawIBAQQg66miXMolEeCzMOIa37NS/ACCgXO/KT6m1PAg/VjP84GhRANCAAQQ6UkO4ptFuuBJuHmCxl7bCyWF3iflKMEBRGVyy6jevaVt1e/9qii9Cb81p67tbILiFHwxQPvmbZpfeaFB3Z0l-----END PRIVATE KEY-----"
Nodeid="10e9490ee29b45bae049b87982c65edb0b2585de27e528c101446572cba8debda56dd5effdaa28bd09bf35a7aeed6c82e2147c3140fbe66d9a5f79a141dd9d25"
Nodecrt="-----BEGIN CERTIFICATE-----MIIBhjCCASygAwIBAgIUOAh5cbUcKbdZhLhLen6qJ9SU1U4wCgYIKoZIzj0EAwIwNzEPMA0GA1UEAwwGYWdlbmN5MRMwEQYDVQQKDApmaXNjby1iY29zMQ8wDQYDVQQLDAZhZ2VuY3kwIBcNMjAxMTAzMDY1ODI3WhgPMjEyMDEwMTAwNjU4MjdaMDQxDjAMBgNVBAMMBW5vZGUwMRMwEQYDVQQKDApmaXNjby1iY29zMQ0wCwYDVQQLDARub2RlMFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEEOlJDuKbRbrgSbh5gsZe2wslhd4n5SjBAURlcsuo3r2lbdXv/aoovQm/Naeu7WyC4hR8MUD75m2aX3mhQd2dJaMaMBgwCQYDVR0TBAIwADALBgNVHQ8EBAMCBeAwCgYIKoZIzj0EAwIDSAAwRQIhAO3MHyVQLQBOF8fLKI17DOevUSP/oh4PVtr8A8IeWi7aAiAXj+DNmLQJvjtJEZM1nJ8emsW7Rz43n/ubaC/ocBr0Zw==-----END CERTIFICATE----------BEGIN CERTIFICATE-----MIIBezCCASGgAwIBAgIUOWWv51vIyS6Zybmr4njwEuU/c60wCgYIKoZIzj0EAwIwNTEOMAwGA1UEAwwFY2hhaW4xEzARBgNVBAoMCmZpc2NvLWJjb3MxDjAMBgNVBAsMBWNoYWluMB4XDTIwMTEwMzA2NTgyN1oXDTMwMTEwMTA2NTgyN1owNzEPMA0GA1UEAwwGYWdlbmN5MRMwEQYDVQQKDApmaXNjby1iY29zMQ8wDQYDVQQLDAZhZ2VuY3kwVjAQBgcqhkjOPQIBBgUrgQQACgNCAARr7JflA87nPQIKj8LrrYiUVxwfyy69M3EKginSdf3iSRHVUZrH8p1KCW+jDaXQt20UThG/wW6/rs9mMZqqs/iyoxAwDjAMBgNVHRMEBTADAQH/MAoGCCqGSM49BAMCA0gAMEUCIQCr6cOr1aZC4I0rP0HopTYW/frlvXFc2ONlLs1N137MugIgaM5BS8d/kILsUHy/YaOWR8KGzYE6Y5I0NP8lTVJUdV8=-----END CERTIFICATE----------BEGIN CERTIFICATE-----MIIBvjCCAWSgAwIBAgIUCf3eT4A7qEMqf7zpE2bNfIUdJAQwCgYIKoZIzj0EAwIwNTEOMAwGA1UEAwwFY2hhaW4xEzARBgNVBAoMCmZpc2NvLWJjb3MxDjAMBgNVBAsMBWNoYWluMCAXDTIwMTEwMzA2NTgyN1oYDzIxMjAxMDEwMDY1ODI3WjA1MQ4wDAYDVQQDDAVjaGFpbjETMBEGA1UECgwKZmlzY28tYmNvczEOMAwGA1UECwwFY2hhaW4wVjAQBgcqhkjOPQIBBgUrgQQACgNCAAQGGZCe8MKPCvWH8CiiQHqefEth8p2Zm+XUFQWyd5NItMm4muyrrIbVcfsxU42p9fowUg5gOhL6HbOHixCeu7bUo1MwUTAdBgNVHQ4EFgQUfMKZqsmwJ08BvgtTwPx+FOwKXTwwHwYDVR0jBBgwFoAUfMKZqsmwJ08BvgtTwPx+FOwKXTwwDwYDVR0TAQH/BAUwAwEB/zAKBggqhkjOPQQDAgNIADBFAiEAyX1YSJ+bw8YJGxARNYlSPPcGojFkab1yhPGCB58bfKsCIDaMaWMAtcBQfup1gqqHvHmMHGhbJVYNs/6+XxHDEhsC-----END CERTIFICATE-----"
Datakey=""
Address=""
def Senddata5():
    #组装json的数据
    data= {\
    "Code":"5",\
    "Timestamp":"20200826095157",\
    "Data":{\
    "Linux_mac":Linux_mac,\
    "Group_id":"1",\
    "Contract_version":"0.1",\
    "Ca_crt":Cacrt,\
    "Node_key":Nodekey,\
    "Node_id":Nodeid,\
    "Node_crt":Nodecrt,\
    "Data_key":Datakey,\
    "Address":Address,\
    }\
    }
    #将数据转为json数据
    datajson = json.dumps(data)
    #发送数据给udp服务器
    return Senddata(datajson)



if __name__ == "__main__":
    recive=Senddata5()
    print (recive)
    
    recive=Senddata1()
    print (recive)

    recive=Senddata2()
    print (recive)
    recive=Senddata3()
    print (recive)
    recive=Senddata4()
    print (recive)
