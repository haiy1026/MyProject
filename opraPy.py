#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   opraPy.py
@Time    :   2020/11/24 08:47:11
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   使用数学函数示例
'''
import math

print(3**4)

print(~2+4)
# 取绝对值函数
print(abs(-9))

# 向上取整函数
print(math.ceil(8.1))

# 取e的幂函数
print(math.exp(3))

# 取绝对值，但是是浮点型
print(math.fabs(-9))

# 向下取舍
print(math.floor(8.8))

# 取log函数
print(math.log(6))

# 取以10为底的函数
print(math.log10(4))

# 返回给定参数的最大值
print(max(2,3,4))

# 返回给定参数的最小值
print(min(3,4,5,6))

# 返回整数和小数部分，都以浮点型表示
print(math.modf(4.5))

# 计算幂函数 x**y
print(pow(3,4))

# 返回四舍五入
print(round(3.2))

# 取平方根
print(math.sqrt(4))
x=4.58888
print(" %2f"%(x))

