# /usr/bin/python
# coding:utf-8

import os
import sys

list = os.listdir('.')
extension = sys.argv[1]
i = 1

for f in list:
    if f == "sort.py":
        continue
    if i < 10:
        os.rename(f, '0'+str(i)+extension)
    else:
        os.rename(f, str(i)+extension)
    i += 1
