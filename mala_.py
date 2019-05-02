import requests
from bs4 import BeautifulSoup
import re
import csv
import time

def get_url(url):
    """获取一个界面的URL"""
    res = requests.get(url)
    demo =res.text
    soup = BeautifulSoup(demo,"html.parser")
    url_all = []
    url_all = re.findall(r'https://www.mala.cn/thread-.{8}-1-.{0,3}.html',str(soup))
    url_all = list(set(url_all))
    return url_all

def get_text(urls,name):
    """获取文本"""
    for url in urls:
        requests.adapters.DEFAULT_RETRIES = 10
        res = requests.get(url)
        demo = res.text
        soup = BeautifulSoup(demo,"html.parser")
        time = []
        title = []
        content = []

        title = soup.find_all('span',attrs= {'id':'thread_subject','style':'display:none'})
        time = soup.find_all('em',attrs= {'id':re.compile("authorposton")})
        content = soup.find_all('div',attrs= {'id':re.compile("copy")})
        null = ["无"]
        all_content = []
        if len(title)!=0:
            all_content.append(title[0].text)
        else:
            all_content.append(null[0])
        if len(time)!=0:
            all_content.append(time[0].text)
        else:
            all_content.append(null[0])
        if len(content)!=0:
            all_content.append(content[0].text)
        else:
            all_content.append(null[0])

        write_into(all_content,name)


def write_into(data,filename_0):
    """写入文件"""
    with open(filename_0,'a',encoding= 'utf-8-sig',newline="") as file_object:
        writer = csv.writer(file_object)
        writer.writerow(data)

if __name__ == '__main__':
    for page_max in range(1,101):
        filename = "mala_shequ"+str(page_max)+".csv"
        url_initial="https://www.mala.cn/forum-5-"+str(page_max)+".html"
        url_page = []
        url_page =  get_url(url_initial)
        get_text(url_page,filename)
        print("第"+str(page_max)+"页。")