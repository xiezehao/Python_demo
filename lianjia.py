import requests
from bs4 import BeautifulSoup
import time

dataSoup=[]
def getDataList(url):
    res=requests.get(url)
    res.encoding="utf-8"
    soup = BeautifulSoup(res.text,'html.parser')
    items = soup.select('.sellListContent li')
    if(len(items)>0):
        print(res.url)
        for item in items:
            img_link=item.select(".lj-lazy")[0]["src"]
            title=item.select(".title a")[0].text
            detail_link=item.select(".title a")[0]["href"]
            positionInfo=item.select(".positionInfo a")[0].text+"-"+item.select(".positionInfo a")[1].text
            houseInfo=item.select(".houseInfo")[0].text
            followInfo=item.select(".followInfo")[0].text
            price=item.select(".totalPrice span")[0].text
            unitPrice=item.select(".unitPrice span")[0].text
            dataSoup.append({
                "img_link":img_link,
                "title":title,
                "detail_link":detail_link,
                "positionInfo":positionInfo,
                "houseInfo":houseInfo,
                "followInfo":followInfo,
                "price":price,
                "unitPrice":unitPrice,
            })
    else:
        print("重新验证:"+url+res.headers)
    
    time.sleep(5)

url="https://gz.lianjia.com/ershoufang/pg{}/"
for i in range(1,5):
    getDataList(url.format(i))

print(len(dataSoup))