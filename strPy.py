#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   strPy.py
@Time    :   2020/11/24 09:36:12
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   字符串类型的操作
'''


# 返回首字母大写
str="hello world"

print("%s"%str.capitalize())

# 截取
print(str[2:4])

if "s" in str:
    print("yes")
elif "l" in str:
    print("在")
else:
    print("Not in")
# 截取
print("%5s"%(str))

# 指定宽度
print(str.center(50))
# 统计在长度为4的字符串中出现l的次数
print(str.count("l",1,5))
# 字符编码 py3中就没有啦
print(str.encode(encoding="utf-8",errors="strict"))

#判断结束的字符 	endswith(suffix, beg=0, end=len(string))
print(str.endswith("l",2,5))

# 查找字符串
print(str.find("l"))

# 取索引
print(str.index("w"))

# 字符串中是否都是数字或者字母类型
print(str.isalnum())

# 字符串中是否都是字母或者中文,空格也返回false
print(str.isalpha())
st2="a bcd"
print(st2.isalpha())
# 都是数字
print("345".isdigit())

# 都是小写
print(str.islower())
print("A".islower())

# 标题化的
print(str.istitle())

# 都是大写
print(str.isupper())

# 拼接，join和”+“
print(",".join(str))

# 返回字符串的长度
print(len(str))

# 左对齐，并且宽度为20
print(str.ljust(20,"\t"))

# 转成小写
print(str.lower())

# 转成大写
print(str.upper())

# 截取
print(str.strip())

st2=" abc"
print(st2.lstrip())

# 转换映射表
print(str.maketrans("l","I"))

# 返回最大的字母
print(max(str))

# 返回最小的字母
print(min("abc"))

# 替换,参数为，要替换的字符，换成的字符和替换的次数
print(str.replace("l","I",1))

# 从右边开始查找
print(str.rfind("l"))
print(str.rindex("l"))

# 右对齐
print(str.rjust(39))
# 删除字符串末尾的空格
print("hello ".strip())
print("hello ")

# 转换
print(str.swapcase())

# 标题化,每个字母的首写是大写
print(str.title())


st2="hello"
st3=st2
print(st2,st3)

st2="world"

print(st2,st3)

import copy 

st3=copy.deepcopy(st2)

print(st3)

print(st3)

name=input("name= ")
age=input("age= ")
job=input("job= ")
sal=input("sal= ")

info='''
-------------info of {_name}-----------
Name:   {_name}
Age:    {_age}
Job:    {_job}
Sal:    {_sal}
'''.format(_name=name,_age=age,_job=job,_sal=sal)

print(info)