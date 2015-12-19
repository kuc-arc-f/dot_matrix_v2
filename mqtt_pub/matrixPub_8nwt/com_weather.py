# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_sensor
class weatherClass:

    def __init__(self):
        print ""
        
    
    def get_wdata(self, city):
    	#sRet=""
    	dic = {"id": 0L, "city" : "", "cond" : "" ,"temp_H" : "", "temp_L" : ""}
    	sSql="SELECT city, cond, TEMP_H, TEMP_L from t_wdat "
    	sSql=sSql+" where CITY='"+ city +"' limit 1"
    	
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	for row in result:
    		dic["city"]          =row[0]
    		dic["cond"]          =row[1]
    		dic["temp_H"]        =row[2]
    		dic["temp_L"]        =row[3]
    	
    	cursor.close()
    	connection.close()
    	return dic

    def delete_dat(self, sCity):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql="delete from t_wdat where CITY='" + sCity +"'"
    	cursor.execute(sSql)
    	connection.commit()
    	connection.close()
    	ret=True
    	return ret

    def saveData(self, getDat ):
    	ret=False
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	sSql=u"INSERT INTO t_wdat (CITY"
    	sSql=sSql+",COND"
    	sSql=sSql+",TEMP_H"
    	sSql=sSql+",TEMP_L"
    	sSql=sSql+",created"
    	sSql=sSql+") values ("
    	sSql=sSql+ " '"+ getDat['location']['city'] +"'"
    	sSql=sSql+ ",'"+ getDat['condition']['text'] +"'"
    	sSql=sSql+ ","+ getDat['forecasts'][1]['high']
    	sSql=sSql+ ","+ getDat['forecasts'][1]['low']
    	sSql=sSql+",now() );"
    	cursor.execute(sSql)
    	connection.commit()
    	cursor.close()
    	connection.close()
    	ret=True
    	return ret
    	