#_*_coding:utf-8_*_
import re
from typing import List, Any

import requests
from bs4 import BeautifulSoup
#引入需要的库

def get_html(url):
    """获取网站的全部内容"""
    try:
      html=requests.get(url)
      html.status_code
      html.encoding=html.apparent_encoding
      return html
    except:
        return("获取网页html失败。")

def get_notices(material):
    """获取网站的公告信息"""
    try:
        demo=material.text
        soup=BeautifulSoup(demo,'html.parser')
        return re.findall(r'.+公告',soup.text)
    except:
        print("获取公告信息失败。")

def put_into_ducument(notice,filename_0):
    """将公告信息存储"""
    try:
        with open(filename_0,'a') as object:
            object.write(notice)
    except:
        print("存储公告信息失败.")

def mian():
    """封装后，做为主函数等待调用"""
    url='http://www.xhu.edu.cn/'
    filename='F:\Python_learning\python_learn1\\first_document.txt'
    result_html=get_html(url)
    result_soup=get_notices(result_html)
    result_soup_0=str(result_soup)
    put_into_ducument(result_soup_0,filename)


boolen=input("你想查询西华大学的公告爱嘛？/n如果想请输入0")
if boolen==0:
    mian()
else:
    pass


