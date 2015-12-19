# -*- coding: utf-8 -*- 
import paho.mqtt.publish as publish
import com_appConst
import com_weather
import time
import com_sendString

#com_mqttPub
class mqttPubClass:

    def __init__(self):
        print ""
        
    def send_pubw(self, sPay ,sTopic):
		clsConst  = com_appConst.appConstClass()
		iWait=0
		iAdd=5
		if (len(sPay) < 1):
			return
		if( len(sPay) > 20 ):
			sPay=sPay[0:20]
		if( len(sPay) > 10 ):
			iAdd=(len(sPay) * 1000) * 0.5
			iAdd=iAdd / 1000
		print("sLen=")
		print(len(sPay))
		#print("sPay=" +sPay)
		publish.single(topic=sTopic, payload=sPay, hostname=clsConst.mMQTT_HostName , port=clsConst.mMQTT_Port )
		print("iWait=")
		iWait = (len(sPay) * clsConst.mWaitMsec) / 1000
		iWait = iWait+iAdd
		print(str(iWait) )
		time.sleep(iWait)
		return
		
    def get_sendWdata(self, sCity ,sTopic ):
		sPay=""
		clsConst  = com_appConst.appConstClass()
		clsWeaher= com_weather.weatherClass()
		clsSend= com_sendString.sendStringClass()
		dic= clsWeaher.get_wdata(sCity)
		print(len(dic))
		print(dic)
		if (len(dic) < 1):
			return
		sTemp="てんき：ふくおか"
		sTemp=clsSend.convert_zenkau( sTemp )
		#city
		self.send_pubw(sTemp ,sTopic)
		#cond
		sTemp=clsSend.convert_zenkau(dic["cond"])
		self.send_pubw(sTemp ,sTopic)
		#temp-H
		print("temp_H=")
		print(str(dic["temp_H"]))
#		sTemp="High Temp:" + str(dic["temp_H"]) + "(C)"
		sTemp= "さいこうきおん:"
		sTemp=clsSend.convert_zenkau( sTemp )
		self.send_pubw(sTemp ,sTopic)
		sTemp= str(dic["temp_H"]) + "(C)"
		sTemp=clsSend.convert_zenkau( sTemp )
		self.send_pubw(sTemp ,sTopic)
		#temp-L
		sTemp="さいていきおん:"
		sTemp=clsSend.convert_zenkau( sTemp )
		self.send_pubw(sTemp ,sTopic)
		sTemp=str(dic["temp_L"]) + "(C)"
		sTemp=clsSend.convert_zenkau( sTemp )
		self.send_pubw(sTemp ,sTopic)
		return