#!/appdir/app/anaconda3/bin python3
# -*- encoding: utf-8 -*-
'''
@File    :   filePy.py
@Time    :   2020/11/24 23:26:14
@Author  :   haiy1026 
@Version :   1.0
@Contact :   531739146@qq.com
@License :   (C)Copyright 2020-2030
@Desc    :   None
'''

with open("test.txt","+w") as f:
    f.write("hello\n")
f.close()

with open("test.txt","r") as f:
    lines=f.readlines()
    for item in lines:
        print(item)
f.close()

# 序列化
import pickle

output=open("pickle.pkl","wb")
with open("test.txt","r") as f:
    data=f.readlines()
    pickle.dump(data,output)
    f.close()

import pprint
files=pickle.load("pickle.pkl")
pprint.pprint(files)