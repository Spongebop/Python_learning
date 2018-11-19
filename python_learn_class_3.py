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


user_0=User('ling','jianhang','19','176')
user_0.describle()
user_0.gereet_user()

class Admin(User):
    """继承USER"""
    def __init__(self,first_name,last_name,age,length):
        """初始化父类的属性"""
        super().__init__(first_name,last_name,age,length)
        self.privileges=['can add post','can delect post','can ban user']

    def show_privileges(self):
        for power in self.privileges:
         print("管理员的作用有"+power)

admin=Admin('Fang','jianping',8,176)
admin.show_privileges()