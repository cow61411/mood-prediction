import os
import re

#set datapath
trainpath = "./../train/"
moodmappath = "./../data_from_kaggle/moods_mapping.txt"
trainlabelspath = "./../data_from_kaggle/train_labels.csv"

'''
# set the dict of moods_mapping
moodmap = {}

f = open(moodmappath , 'r')
f.readline()
content = f.readlines()
for line in content:
    line = line.replace("\n" , "")
    key , value = line.split(",")
    moodmap[key] = value
f.close()
'''

#set the dict of train_labels
trainlabels = {}

f = open(trainlabelspath , 'r')
f.readline()
content = f.readlines()
for line in content:
    line = line.replace("\n" , "")
    key , value = line.split(",")
    trainlabels[key] = value
f.close()

'''
for dirs , root , files in os.walk(trainpath):
    for filename in files:
	f = open(trainpath + filename , 'r')
	content = f.read()
	content = re.sub('<[^>]*>' , '' ,content)
	print content
	f.close()
'''
