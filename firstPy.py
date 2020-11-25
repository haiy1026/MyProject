#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   firstPy.py
@Time    :   2020/11/23 21:43:37
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   None
'''

import keyword

print(keyword.kwlist)


ll=keyword.kwlist

for item in ll:
    print(item)



if True:
    print ("True")
else:
    print ("False")


v1=0
v2=9
v3=9
item=v1+\
    v2+\
    v3

print(item)

arg=input("arg=请输入")

print("你输入的是："+arg)

