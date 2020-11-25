#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   hello.py
@Time    :   2020/11/23 21:43:22
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   None
'''

print(isinstance(1,int))
print (type(1))

print(9/4)
print(9//4)
print(1/3)

print("\n")
print(r"\n")


aa=['1','2','3','4']
print(aa[-3])

print(aa.append(8))
print(aa.pop(3))

print(aa)
print(aa[1:2:3])

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'baidu',"baidu"}

print(set(sites))

a = set('abracadabra')
b = set('alacazam')

print(a-b)
print(a|b)

print(a^b)