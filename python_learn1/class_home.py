class User():
    """用户名的创立"""

    def __init__(self,first_name,last_name,age,length):
        """参数的传入"""
        self.firsr_name=first_name
        self.last_name=last_name
        self.age=age
        self.length=length

    def describle(self):
        self.complect_name=self.firsr_name+self.last_name
        print("This man name is "+self.complect_name+".")

    def gereet_user(self):
        """问候用户"""
        print("hello!"+self.complect_name)


class Admin(User):
    """继承USER"""
    def __init__(self,first_name,last_name,age,length):
        """初始化父类的属性"""
        super().__init__(first_name,last_name,age,length)
        self.privileges=['can add post','can delect post','can ban user']

    def show_privileges(self):
        for power in self.privileges:
            print("管理员的作用有"+power)

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
