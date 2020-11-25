#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   tuplePy.py
@Time    :   2020/11/24 11:16:32
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   元组
'''

t1 = ('Google', 'Runoob', 1997, 2000)
t2 = (1, 2, 3, 4, 5, 6, 7 )
# 元组长度
print(len(t1))
# 不可修改，但是可以拼接
print(t1+t2)

# 字典
s1= {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

s2=s1.copy()

s3=s1.fromkeys("Name")
print(s3)
