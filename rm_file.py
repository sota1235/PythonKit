# encoding:utf-8

import os

for i in range(14):
    for j in range(12):
        for h in range(50):
            os.remove("./Photo/"+str(2000+i)+"/"+str(j+1)+"月/"+"picture"+str(h)+".img")
