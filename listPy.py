#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   listPy.py
@Time    :   2020/11/24 10:56:22
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   列表操作
'''

l1=[1,2,3,3,4,5]
l2=[4,5,6,7,8]
# 删除
del l1[3]
print(l1)


l3=l1+l2
print(l3)

# 取列表长度
print(len(l3))
# 取最大的
print(max(l1))

# 将元组转换成列表
print(list((1,2,3)))

# 添加对象
print(l1.append(9))
l1.append(9)
print(l1)

# 计数
print(l2.count(5))

# 插入
print(l1.insert(4,2))
print(l1)

# 弹出
l1.pop(5)
print(l1)

# 反转
print(l1.reverse())
print(l1)

# 排序
print(l1.sort())

print(l1)