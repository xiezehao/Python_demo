import requests
from bs4 import BeautifulSoup

res = requests.get("http://pic.netbian.com/4kmeinv/")
#res.encoding="utf-8"
#res.encode("ISO-8859-1").decode("utf-8")
#print(res.text.encode("ISO-8859-1").decode("gbk"))
soup = BeautifulSoup(res.text.encode("ISO-8859-1").decode("gbk"),'html.parser')
#print(soup.select(".clearfix li"))
for item in soup.select(".clearfix li"):
    #http://pic.netbian.com/uploads/allimg/180128/112234-1517109754fad1.jpg
    url = "http://pic.netbian.com"+item.select("img")[0]["src"]
    name = item.select("img")[0]["src"].split("/")[-1]
    ir = requests.get(url, stream=True)
    if ir.status_code == 200:
        open(name,'wb').write(ir.content)

