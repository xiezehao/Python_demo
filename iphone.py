import re
import requests
import json
import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='python'
)
cursor = connection.cursor()
sql="INSERT INTO `iphone` (`nickname`,`content`,`creationTime`) VALUES (%s,%s,%s)"

def getData(url):
    headers={
        'accept':'*/*',
        'Referer':'https://item.jd.com/100000177760.html#comment',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    res = requests.get(url,headers = headers)
    
    #res.encoding='utf-8'
    response=json.loads(res.text.lstrip('fetchJSON_comment98vv50419(').rstrip(');'))
    
    #print(type(response['comments']))
    for item in response['comments']:
        #print(item['nickname'],item['content'],item['creationTime'])
        cursor.execute(sql,(item['nickname'],item['content'],item['creationTime']))
    connection.commit()


url="https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv50419&productId=100000177760&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1"
getData(url)
connection.close()