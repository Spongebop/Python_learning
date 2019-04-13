# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
import csv
import eventlet

def getsourcepage(url):
    """获取网页源码"""
    brower = webdriver.Firefox(executable_path='geckodriver')
    brower.get(url)
    time.sleep(3)
    brower.find_element_by_xpath('//input[@id="loginname"]').click() #点击登陆框
    brower.find_element_by_xpath('//input[@id="loginname"]').send_keys("17381596318")
    brower.find_element_by_css_selector(".password > div:nth-child(1) > input:nth-child(1)").click()
    brower.find_element_by_css_selector(".password > div:nth-child(1) > input:nth-child(1)").send_keys("1461128650") #输入密码
    brower.find_element_by_css_selector("div.info_list:nth-child(6)> a:nth-child(1)").click()
    brower.find_element_by_css_selector("div.info_list:nth-child(6)> a:nth-child(1)").click() #登陆
    time.sleep(3) #等待网页缓存
    return brower

def getsourcepage_new(driver,pages,key_words):
    """关键字搜索"""
    driver.get("https://s.weibo.com/") #打开搜索页面
    eventlet.monkey_patch()
    time.sleep(3)
    for word in key_words:
        filename_0 = word +".csv"
        for page in range(1,pages):  #page设置爬取的页数
            with eventlet.Timeout(3,False):
                 driver.get("https://s.weibo.com/weibo?q="+word+"&Refer=index$&page="+str(page)) #关键字四川可用字符串代替
                 content = driver.page_source
                 soup = BeautifulSoup(content,'html.parser')
                 all_Username=[]
                 all_Time = []
                 all_Messages = []
                 all_nokey = []
                 all_Messages = soup.find_all('p',attrs = {'class':'txt','node-type':'feed_list_content'})
                 all_Time = soup.find_all('a',attrs = {'target':'_blank','suda-data':re.compile('click:.{0,3}wb_time')})
                 all_Username = soup.find_all('a',attrs= {'class':'name'})
                 all_nokey = soup.find_all('div',attrs={'class':'card card-no-result s-pt20b40'})

                 if (len(all_nokey)==0):
                     try:
                         write_document(filename_0,all_Messages,all_Time,all_Username)
                     except:
                         pass
            #数据获取完成
                 else:
                     break
             #由于微博极少部分数据结构复杂，溢出抛去

def write_document(filename_0,messages_0,times_0,username_0):
    """写入方法"""
    with open(filename_0,'a',encoding= 'utf-8-sig') as file_object:
        writer = csv.writer(file_object)
        circle = 0
        byte = len(messages_0)
        while (circle < byte ):
            data = []
            data.append(username_0[circle].text.strip())
            data.append(messages_0[circle].text.strip())
            data.append(times_0[circle].text.strip())
            writer.writerow(data)
            circle +=1

def  key_words():
    """处理关键词"""
    key_words = []
    key_head = ["四川","自贡","攀枝花","泸州","德阳","绵阳","广元","遂宁","内江","资阳","乐山","眉山","南充","宜宾","广安","达州","巴中","雅安","甘孜","阿坝","凉山","成都"]
    key_words_bady = ["K粉","霸凌","霸占","白粉","绑架","保护费","保护伞","引爆","燃爆","爆破","防爆","爆炸","暴动","暴君","暴行","被抓","逼供","逼迫","逼迁","藏独","超载","车祸",
                  "持刀","持械","传销","串供","刺杀","村霸","错案","打110","打死","弹药","地头蛇","堵路","对峙","恶霸","恶行","法轮功","犯法","诽榜","公安","勾结","海洛因","黑道",
                  "黑恶","黑老大","黑钱","黑社会","黑势力","黑手","伙同","击毙","羁押","集资","挟持","假案","假释","拒捕","恐吓","扣留","扣押","狂殴","滥用","勒索","轮奸","裸死","卖淫",
                  "灭口","民间借贷","命案","谋杀","闹访","闹事","虐待","虐童","殴打","派出所","嫖","潜逃","枪","强暴","强拆","强奸","强占","抢掠","抢烧","囚禁","群架","群殴","扰乱","扰民",
                  "人命","骚乱","杀人","煽动","烧毁","烧杀","身亡","施暴","示威","死伤","死亡","死刑","伤亡","索赔","射杀","逃逸","讨公道","挑衅","跳河","跳楼","通缉","脱罪","外逃",
                  "枉法","威胁","为非作歹","围攻","围殴","维权","伪造","伪证","猥亵","窝藏","诬告","诬蔑","诬陷","武力","袭民","陷害","销赃","泄密","械斗刑讯","凶器","血案","寻衅",
                  "徇私","用刑","游行","诈骗","招妓","追诉","坠楼","滋事","自焚","自杀","纵火","走私","叛乱","空袭","暴力","砍人","砍杀","杀戮","血腥","暴袭","滥杀","暴乱","绞死",
                  "抛尸","遭袭","踩踏","叫嚣","遭分尸","屠杀","炸毁","枪击","焚烧","枪杀","恶性恐怖","非法组织","群体事件","镇压","造反","黑团伙","炸弹","黑火药","炸药","开枪","暗杀","报复社会",
                  "疆独","藏独","民族矛盾","民族歧视","民族分裂","冲突","绿教","绿绿","伊斯兰","回民","清真","宗教","罢工","绑架","暴动","暴乱","爆炸","持刀","枪","打架","打人","闹事","强拆","煽动",
                  "上访","访民","游行","跳楼","横幅","医闹","抵制","示威","维权","集会","讨薪","征集签名","再聚天安门","民主斗争","京访","人权斗争","罢课","堵路","喊冤","闹访","信访","截访","拦访","群访",
                  "集体访","越级访","重复访","检举","揭发","请愿","抗议","静坐","自焚","下跪","拘禁","打击报复","没人管","管不管","不受理","不解决","不作为","执法态度","投诉","举报","申诉",
                  "军人","涉军","伤残","两参","复员","转移","安置","部队","军转","退伍","退役","士兵","老兵","士官","解放军","抗战","战士","上访","信访","群工局","群工部","访民","截访","拦访","群访","申诉",
                  "举报","检举","揭发","请愿","抗议","游行","集会","静坐","自焚","下跪","拘禁","强拆","罢工","报复","维权","投诉","聚集","堵路"]
    for head in key_head:
        for bady in key_words_bady:
            key_words.append(head+bady)
    return key_words
if __name__ == '__main__':
    no_use = "搜索不了的关键词"
    url = "http://www.weibo.com/login.php"
    pages = 3
    driver = getsourcepage(url)
    key_words = key_words()
    getsourcepage_new(driver,pages,key_words)




