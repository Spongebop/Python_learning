import  requests
filename='https://www.icourse163.org/learn/BIT-1001870001?tid=1003245012#/learn/content?type=detail&id=1004574440'
filename_0="https://www.baidu.com/s"
#伪装为游览器，headers实现
try:
 kv={'user-agent':'Mozilla/5.0'}
 r=requests.get(filename,headers=kv)
 r.raise_for_status()
 r.encoding=r.apparent_encoding
 print(r.request.headers)

except:
 print("爬取失败。")


#关键字的更改
keyword="Python"
try:
 kv={'wd':keyword}
 r=requests.get(filename_0,params=kv)
 r.raise_for_status()
 print(r.request.url)
except:
 print("爬取错误。")
