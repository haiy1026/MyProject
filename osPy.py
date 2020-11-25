#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   osPy.py
@Time    :   2020/11/25 08:29:27
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   None
'''

import os as oos

# 当前路径是否可以访问

# os.F_OK: 作为access()的mode参数，path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， path是否可读。
# os.W_OK 包含在access()的mode参数中 ， path是否可写。
# os.X_OK 包含在access()的mode参数中 ，path是否可执行。

print(oos.access("/appdir/codes/pythonCodes/MyProject/firstPy.py",mode=oos.F_OK))

