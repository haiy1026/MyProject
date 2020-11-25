#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   setPy.py
@Time    :   2020/11/24 20:25:03
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   集合的操作
'''

s = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
s.add("huawei")

print(s)

s2=s.copy()
s2.add("tence")
print(s2)
s3=s
print(s3)
# 返回多个集合的差集
print(s.difference(s2))

s4=s2.difference(s3)
print(s4)

# 移除集合中的元素，该元素在指定的集合也存在。
s5=s.difference_update(s3)

print(s5)

s=s2.discard("orange")
print(s)


print(s3.isdisjoint(s2))

s5={'apple', 'orange'}
print(type(s5))
print(type(s))


print(s5.pop())

for i in range(5):
    print(i,end=" ")