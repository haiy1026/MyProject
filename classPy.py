#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   classPy.py
@Time    :   2020/11/25 08:48:13
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   支持面向对象编成
'''

class People:
    # 基本属性
    name=""
    age=0
    # 定义私有属性
    __weight=0
    def __init__(self,n,a,w): # 定义构造函数
        self.name=n
        self.age=a
        self.__weight=w
    
    def speak(self):
        print("{} 说： 我 {} 岁了".format(self.name,self.age))


p=People("haiy",28,120)
p.speak()

# 继承
class Student(People):
    grage=0
    def __init__(self,n,a,w,g):
        People.__init__(self,n,a,w)
        self.grage=g
    def speak(self):
        print("{}说，我{}岁了，读{}年级了".format(self.name, self.age, self.grage))


stu=Student("小子",29,120,3)
stu.speak()


# 另个类
class Speaker:
    topic=""
    name=""
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print("我叫 {} ，是一个演说家，演讲的题目是{}".format(self.name,self.topic))


s=Speaker("小子","python")
s.speak()


# 多重继承
class Sample(Speaker,Student):
    a=""
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)
    
    # 重写speak方法
sam=Sample("小x",29,120,3,"python")
sam.speak()  #不重写方法,会调用括号中最前面的父类方法

# 多重继承
class Sample2(Speaker,Student):
    a=""
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)
    def speak(self): #重写父类方法
        print("我叫 {} ，今年读{}年级,是一个演说家，演讲的题目是{}".format(self.name,self.grage,self.topic))

s2=Sample2("小x",29,120,3,"python")
s2.speak()