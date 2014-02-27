# /usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

argvs = sys.argv
count = argvs[1]

# 第一引数:作る数 第二引数:(あれば)末尾につけるやつ
for i in range(count):
    os.mkdir(str(i)+argv[2])
