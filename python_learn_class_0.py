class Restautant():
    """"餐厅的类实化"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_servedd=0

    def describe_resturant(self) :
        """打印前两个餐馆消息"""
        print("Resturant name is " + self.restaurant_name + ",and his type is " + self.cuisine_type + ".")

    def open_resturant(self):
        """说出现在餐厅是否在开业状态中"""
        print("目前餐厅在开业状态")
    def number_served(self):
        """反馈出有多少人就餐"""
        print("这里已经有"+str(self.number_servedd)+"就餐过了。")

    def set_number_server(self,number):
        """重写就餐人数"""
        self.number_servedd=number

    def increamenr_number_served(self,add_number):
        """增加每天来的客人数目"""
        self.number_servedd+=add_number

resturant_0= Restautant("shagou",'kuaican')
resturant_0.open_resturant()
resturant_0.describe_resturant()

resturant_1=Restautant('汉堡王','快餐')
resturant_1.describe_resturant()

resturant_2=Restautant('华莱士','外卖')
resturant_2.describe_resturant()


resturant=Restautant('zhangjiekairou','kuacan')
resturant.set_number_server(23)
resturant.increamenr_number_served(2)
resturant.number_served()
resturant.describe_resturant()




