# coding:utf-8

import os

list = os.listdir('.')
i = 1

for i in list:
    if i < 10:
        os.rename(i, '0'+str(i))
    else:
        os.rename(i, str(i))
    i += 1
