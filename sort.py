# /usr/bin/python
# coding:utf-8

# 第一引数:拡張子

import os
import sys

list = os.listdir('.')
extension = sys.argv[1]
i = 1

for f in list:
    if f == "sort.py":
        continue
    os.rename(f, str(i)+extension)
    i += 1
