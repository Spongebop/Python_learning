#图片的爬取和储存
import requests
import  os
url="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%B0%8F%E9%BB%84%E4%BA%BA&hs=2&pn=1&spn=0&di=64460&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cl=2&lm=-1&cs=1992083600%2C3803617825&os=2081354224%2C3801857393&simid=4080921886%2C495359666&adpicid=0&lpn=0&ln=30&fr=ala&fm=&sme=&cg=&bdtype=0&oriquery=%E5%B0%8F%E9%BB%84%E4%BA%BA&objurl=http%3A%2F%2Fimg.tupianzj.com%2Fuploads%2Fallimg%2F140617%2F1-14061GH55V60.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bp7rtwgz3_z%26e3Bv54AzdH3FktzitAzdH3FDNhwp5g2AzdH3F8al8d_z%26e3Bip4s&gsm=0&islist=&querylist="
root="F：\\Python_learning\\python_learn1"
path=root+url.split('/')[-1]
try:
     if not  os.path.exists(root):
        os.mkdir(root)
     if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
     else:
        print("文件已经存在")
except:
    print("爬取失败。")
