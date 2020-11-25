#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   iterNextPy.py
@Time    :   2020/11/24 20:58:45
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   None
'''
import sys

# list=[1,2,3,4]

# it=iter(list)
# print(next(it))

# # 可用for
# for i in it:
#     print(i)

# # 或者用next
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# 返回数字的迭代器
# class MyNum:
#     def __iter__(self):
#         self.a=1
#         return self
    
#     def __next__(self):
#         if self.a<=20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
        

# print("haha ")
# mc=MyNum()

# miter=iter(mc)

# for i in range(24):
#     print(next(miter))




# 生成器 yield实现

def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter >n):
            return
        yield a

        a,b=b,a+b
        counter+=1
f=fibonacci(10)

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()