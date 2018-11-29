import  re
import  requests

url='http://www.ivsky.com/tupian/xiaohuangren_t21343/'
#存储访问的网址（url）
wb_date=requests.get(url).text
#传为文本文件（模拟游览器请求资源）
res=re.compile(r'src="(.+?.jpg)"')
#正则表达式按照要求查找需要的信息
#.+?匹配一切，r用作正则
reg=re.findall(res,wb_date)#findall(要求，范围)
