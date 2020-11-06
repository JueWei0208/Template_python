#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json
#查询人脸设备绑定的信息

#HTTPIP="192.167.111.1"
HTTPIP="127.0.0.1"
HTTPPORT="8889"
TokenAndFaceMac="3333"
api_version="0.1"
#查询人脸设备的信息
def SenddataCWRServiceQueryFaceEquipmentBinding():
    url = "http://"+ HTTPIP+ ":"+ HTTPPORT+"/CWRService/QueryFaceEquipmentBinding"
    #http://192.168.8.210:8889/CWRService/QueryFaceEquipmentBinding
    data = {"device_vendor":"assem","device_mac":TokenAndFaceMac,"device_sn":"123456","device_type":"face","system_info":"linux"}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text


#查询人脸设备的网络状态
def SenddataCWRServiceQueryFaceEquipmentNetworkStatus():
    url = "http://"+ HTTPIP+ ":"+ HTTPPORT+"/CWRService/QueryFaceEquipmentNetworkStatus"
    #http://192.168.8.210:8889/CWRService/QueryFaceEquipmentNetworkStatus
    data = {"device_mac":TokenAndFaceMac}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#获取配置文件
def SenddataBCServiceGetInitConf():
    httpurl = "http://"+HTTPIP+":"+HTTPPORT+"/BCService/GetInitConf"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={"device_vendor":"assem","device_mac":TokenAndFaceMac,"device_sn":"123456","device_type":"face", "system_info":"linux","direction":"in"}
    res = requests.post(url=httpurl,data=json.dumps(data))
    return res.text

#心跳
def SenddataBCServiceHeartBeat():
    url = "http://"+HTTPIP+":"+HTTPPORT+"/BCService/HeartBeat"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#获取人员列表散列值
def SenddataBCServiceQueryEmpHash():
    url = "http://"+HTTPIP+":"+HTTPPORT+"/BCService/QueryEmpHash"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#获取项目人员信息
def SenddataBCServiceQueryEmpList():
    url = "http://"+HTTPIP+":"+ HTTPPORT+"/BCService/QueryEmpList"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#获取人员信息
def SenddataBCServiceQueryEmpInfo():
    url = "http://"+HTTPIP+":" + HTTPPORT+"/BCService/QueryEmpInfo"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={"employee_list":[{"emp_id":"1"}],"facephoto_mode":"url"}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#考勤记录上传
def SenddataBCServiceAddAttendance():
    url = "http://"+HTTPIP+":" + HTTPPORT+"/BCService/AddAttendance"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={"employee_list":[{"emp_id":"1","passed_time":"1000","direction":"in","site_photo":"123","gps":"jx"}]}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#考勤记录确认查询
def SenddataBCServiceTransVerify():
    url = "http://"+HTTPIP+":" + HTTPPORT+"/BCService/TransVerify"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={"trans_code":"0x0382637ff55db8d1aa910ab75d80ab9fd7bfc48c5c8c676fa9696b52a6fd0941"}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text

#软件升级查询
def SenddataBCServiceQuerySoftUpgrade():
    url = "http://"+HTTPIP+":" + HTTPPORT+"/BCService/QuerySoftUpgrade"+"?"+"token="+TokenAndFaceMac+"&"+"api_version="+api_version
    data ={"module":"2","vendor":"2","type":"software","version":"0.1"}
    res = requests.post(url=url,data=json.dumps(data))
    return res.text



if __name__ == "__main__":
    recive=SenddataCWRServiceQueryFaceEquipmentBinding()
    print (recive)
    
    #http的bug
    #SenddataCWRServiceQueryFaceEquipmentBinding马上SenddataBCServiceGetInitConf 不能连续请求

    recive=SenddataBCServiceGetInitConf()
    print (recive)
    
    recive=SenddataCWRServiceQueryFaceEquipmentNetworkStatus()
    print (recive)




