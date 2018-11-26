import  requests
from bs4 import  BeautifulSoup
url="https://jingyan.baidu.com/article/6525d4b14ae078ac7c2e9472.html"
r=requests.get(url)
print(r.text)
