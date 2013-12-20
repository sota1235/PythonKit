# -*- coding utf-8 -*-

# Created by sota1235
# Date 2013/12/20
# This program opens file

import sys

f = open(sys.argv[1],'r')

for line in f:
    print line

