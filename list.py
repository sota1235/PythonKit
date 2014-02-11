import os

list = os.listdir('../Scores/')
f = open('score_list','a')

for line in list:
    f.write(line + '\n')

f.close()
