# -*- coding: utf-8 -*- 
import MySQLdb
import com_appConst
#define


#com_news
class newsClass:

    def __init__(self):
        print ""
        
    
    def get_newsData(self, iMax):
    	#sRet=""
    	ret=[]
    	dic = {"id": 0L, "title" : "" }
    	sSql="SELECT title  from t_news order by id ASC limit " +str(iMax)
    	
    	clsConst = com_appConst.appConstClass()
    	connection = MySQLdb.connect(host=clsConst.mHost, db=clsConst.mDB_NAME, user=clsConst.mUser, passwd=clsConst.mPass, charset="utf8")
    	cursor = connection.cursor()
    	cursor.execute( sSql )
    	result = cursor.fetchall()
    	for row in result:
    		dic = {"id": 0L, "title" : "" }
    		dic["title"]          =row[0]
    		ret.append(dic)
    	
    	cursor.close()
    	connection.close()
    	return ret
