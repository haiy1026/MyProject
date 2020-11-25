#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   funPy.py
@Time    :   2020/11/24 22:34:33
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   函数，传递的是可变对象和不可変对象
'''

"""
开辟空间后，所指内存地址不变，值改变而已

"""
import sys
import hello

def changeLocation(a):
    print(id(a))
    a=10
    print(id(a))

a=1
print(id(a))

changeLocation(a)

# 不定长的参数

def functionname(arg1, *var_args_tuple ):
    "打印输入的参数"
    print("输出 ")
    print(arg1)
    print(var_args_tuple)
print(70,89,98,87)

def func(a,b,*,c):
    # *后面的* 必须传入
    print(a+b+c)
func(2,3,c=5)
# func(1,2,3) #报错

def func2(a):
    print(4)
func2(9)


#匿名函数 lambda实现

sumfunc=lambda arg1,arg2:arg1+arg2
print(sumfunc(3,4)) 


if __name__=="__main__":
    print("hello")