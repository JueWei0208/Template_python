#!/usr/bin/python
# -*- coding=utf-8-*-
import sys
import time
#加入文件的路径 相对路径都是以main函数为依据的 目录的名字
sys.path.append('./Senddata')
sys.path.append('./Senddatahttp')

#from 后面跟文件的名字 import 后面是类的名字
import SendDatostoUDP
import Senddatahttp

if __name__ == "__main__":

    start="start"
    print (start)
    #需要先发送人脸设备的ip bcos的goupid的信息过去
    #这个流程是先启动了成功了bcos的成功之后，在发送这个命令
    res =SendDatostoUDP.Senddata5()
    print (res)
	
    time.sleep(2)
	
    
    #人脸设备绑定
    res =SendDatostoUDP.Senddata1()
    print (res)
    time.sleep(2)
	
    
    #人脸设备软硬件信息上报
    res =SendDatostoUDP.Senddata2()
    print (res)

    #人脸设备外网状态上报
    res =SendDatostoUDP.Senddata3()
    print (res)

    #人脸设备心跳上报
    res =SendDatostoUDP.Senddata4()
    print (res)

    #获取配置文件
    res =Senddatahttp.SenddataBCServiceGetInitConf()
    print (res)

    #心跳
    res =Senddatahttp.SenddataBCServiceHeartBeat()
    print (res)
    
    #获取人员列表散列值
    res =Senddatahttp.SenddataBCServiceQueryEmpHash()
    print (res)
    
    #获取项目人员信息
    res =Senddatahttp.SenddataBCServiceQueryEmpList()
    print (res)
    
    #获取人员信息
    res =Senddatahttp.SenddataBCServiceQueryEmpInfo()
    print (res)

    #考勤记录上传
    res =Senddatahttp.SenddataBCServiceAddAttendance()
    print (res)


    #考勤记录确认查询
    res =Senddatahttp.SenddataBCServiceTransVerify()
    print (res)

    #软件升级查询
    res =Senddatahttp.SenddataBCServiceQuerySoftUpgrade()
    print (res)


   
    time.sleep(4)
    #查询人脸设备的网若状态
    res =Senddatahttp.SenddataCWRServiceQueryFaceEquipmentNetworkStatus()
    print (res)


    #查询人脸设备的绑定信息
    res =Senddatahttp.SenddataCWRServiceQueryFaceEquipmentBinding()
    print (res)


    end="end"
    print (end)
