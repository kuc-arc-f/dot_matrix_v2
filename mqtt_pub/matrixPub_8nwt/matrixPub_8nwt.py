# -*- coding: utf-8 -*- 
#------------------------------------
# @calling
# @purpose : Time/Weather/News Publish(MQTT)
# @date : 2015-12-18
# @Author : Kouji Nakashima / kuc-arc-f.com
#------------------------------------
import paho.mqtt.publish as publish
import datetime
import time
import sys
import traceback
import com_appConst
import com_news
import com_mqttPub
import com_sendString
import zenhan

mTopic="item-kuc-arc-f/device-1/matrix_v2_1"

mTimeMax=5
mMaxTitle=10

mTyp_WDAT =1
mTyp_TIME =2
mTyp_NEWS =3

	
def proc_newsPub(items, sHHMM):
	clsPub=com_mqttPub.mqttPubClass()
	clsSend= com_sendString.sendStringClass()
	for item in items:
		sTitle=  clsSend.convert_zenkau(item)
		#print( "item="+ item)
		clsPub.send_pubw(sTitle ,mTopic)

if __name__ == "__main__":
	clsSend= com_sendString.sendStringClass()
	clsPub=com_mqttPub.mqttPubClass()
	from datetime import datetime
	tmBef = datetime.now()
	iTyp=mTyp_TIME
	while True:
		tmNow = datetime.now()
		tmSpan = tmNow - tmBef
		iSpan = tmSpan.total_seconds()
		time.sleep(1.0)
		sTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		#sHHMM = datetime.now().strftime("%H:%M")
		sTemp=""
		print("time=" +sTime)
		if iSpan > mTimeMax:
			tmBef = datetime.now()
			try:
				clsNews= com_news.newsClass()
				items = clsNews.get_newsData( mMaxTitle )
				for item in items:
					sHHMM = datetime.now().strftime("%H:%M")
					sTemp=clsSend.convert_zenkau("じかん　"+ sHHMM)
					clsPub.send_pubw(sTemp ,mTopic)
					time.sleep(2.0)
					clsPub.get_sendWdata("Fukuoka", mTopic)
					time.sleep(2.0)
					sTemp=clsSend.convert_zenkau("News:")
					clsPub.send_pubw(sTemp ,mTopic)
					sTitle=item["title"]
					lst=clsSend.get_List( sTitle )
					proc_newsPub(lst ,sHHMM)
			except:
				print "--------------------------------------------"
				print traceback.format_exc(sys.exc_info()[2])
				print "--------------------------------------------"
	


