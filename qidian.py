import requests
from bs4 import BeautifulSoup
import pandas

dataSoup=[]
def getDetail(url):
    res= requests.get(url)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    
    for li in soup.select('.book-img-text li'):
        
        title=li.select('h4 a')[0].text
        detail_link = li.select('h4 a')[0]['href']
        img_link = li.select('.book-img-box img')[0]['src']
        author = li.select('.name')[0].text
        typeStr = li.select('.author a')[1].text 
        status = li.select('.author span')[0].text 
        contents = li.select('.intro')[0].text.strip()
        update_title = li.select('.update a')[0].text
        update_time = li.select('.update span')[0].text
        #yuepiao = li.select('.vsuXpdxs')
        dataSoup.append({
            'title':title,
            'detail_link':detail_link,
            'img_link':img_link,
            'author':author,
            'typeStr':typeStr,
            'status':status,
            'contents':contents,
            'update_title':update_title,
            'update_time':update_time,
        })
    #print(dataSoup)
    #return dataSoup
    
        
        
url='https://www.qidian.com/rank/yuepiao?style=1&page={}'
for i in range(1,2):
    getDetail(url.format(i))
#print(len(dataSoup))
pandas.DataFrame(dataSoup)
newform=pandas.DataFrame(dataSoup)
newform.to_excel('newform1.xlsx')