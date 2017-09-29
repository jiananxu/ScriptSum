#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/9/29 9:26
# @Author  : xujn
# @Version : 1.0

from os import walk
import os
import sys
sys.path.append(r'C:\Users\xujn\Desktop\联通项目\脚本\ScriptSum\Biliing-1502')
print (sys.path)

f = []
for (dirpath, dirnames, filenames) in walk(os.getcwd()):
    f.extend(filenames)
    break

print(f)
print(os.listdir(os.getcwd()))
print ((os.getcwd()).replace("\\","/"))
str1 = 'C:\cdce\rcdcd\c'

r = str1.replace("\\",'/')
print (str1)