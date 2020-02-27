import requests
from bs4 import BeautifulSoup
import json
import time
from multiprocessing import Pool

def html_parser(html):
    dataSoup=[]
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.select("dd"):
        sort=item.select(".board-index")[0].text.strip() #排序
        board=item.select(".board-img")[0]["data-src"] #电影图片
        name=item.select(".name a")[0].text.strip() #电影名
        star=item.select(".star")[0].text.strip() #主演
        releasetime=item.select(".releasetime")[0].text.strip() #上映时间
        score=item.select(".integer")[0].text+item.select(".fraction")[0].text.strip() #评分

        dataSoup.append({
            "sort":sort,
            "board":board,
            "name":name,
            "star":star,
            "releasetime":releasetime,
            "score":score,
        })
    return dataSoup

def get_detail(url):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
    }
    res= requests.get(url,headers=headers)
    return res.text

def write_to_file(result):
    with open('result1.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(result,ensure_ascii=False)+'\n')

def main(offset):
    url="https://maoyan.com/board/4?offset="+str(offset)
    html=get_detail(url)
    result= html_parser(html)
    for item in result:
        write_to_file(item)

if __name__ == "__main__":
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)