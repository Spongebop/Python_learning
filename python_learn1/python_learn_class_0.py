class Restautant():
    """"餐厅的类实化"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self) :
        """打印前两个餐馆消息"""
        print("Resturant name is " + self.restaurant_name + ",and his type is " + self.cuisine_type + ".")

    def open_resturant(self):
        """说出现在餐厅是否在开业状态中"""
        print("目前餐厅在开业状态")


resturant_0= Restautant("shagou",'kuaican')
resturant_0.open_resturant()
resturant_0.describe_resturant()

resturant_1=Restautant('汉堡王','快餐')
resturant_1.describe_resturant()

resturant_2=Restautant('华莱士','外卖')
resturant_2.describe_resturant()
