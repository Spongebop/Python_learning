#邀请来聚餐的朋友
Foodlist=['gongzheng','lirui','wuyanjie']
print("i invited"+Foodlist[0]+"to eat dilishers!")
print("i invited"+Foodlist[1]+"to eat dilishers!")
print("i invited"+Foodlist[2]+"to eat dilishers!")
#有原因不能来的朋友
he=Foodlist.pop(1)
print("becuase lirui in American,and "+he+" can not togetshr tonight.")
Foodlist.insert(1,'nixubo')
print("i invited"+Foodlist[0]+"to eat dilishers!")
print("i invited"+Foodlist[1]+"to eat dilishers!")
print("i invited"+Foodlist[2]+"to eat dilishers!")
#来的人变多了，换了个更大的桌子
print("i find a bigger table than before,so i intend to invite more friendas come to here.")
Foodlist.append('huji')
Foodlist.append('zhoumingyan')
Foodlist.append('panyicheng')
#最后聚餐的同学名单
print(Foodlist)




