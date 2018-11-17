class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self,name,age):
        """初始化属性name and age"""
        self.name=name
        self.age=age

    def sit(self):
        """模拟小狗的命令蹲下"""
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        """模拟小狗被咬命令时打滚"""
        print(self.name.title()+"rolled over and its age is "+self.age+".")


my_dog=Dog('white',20)
print("my dog name is "+my_dog.name.title()+".")
print("my dog is "+str(my_dog.age)+"yesrs old.")
