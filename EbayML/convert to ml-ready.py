import pickle
import sys
import gensim
import string
import time
from copy import deepcopy
from sklearn import preprocessing
import tensorflow as tf
import numpy as np
wordfile ="words.pk1"
wordstore = open(wordfile, 'rb')
wordtrain = pickle.load(wordstore)
wordstore.close()
trainsentences = []
for item in wordtrain:
    lowercase = item.lower()
    split = lowercase.split()
    trainsentences.append(split)
model = gensim.models.Word2Vec(trainsentences, min_count = 400, size = 10, alpha = .025, iter = 400 )
dbfile ="ebaydata.pk1"
def openebaydata():
    dbstore = open(dbfile, 'rb')
    global datadump
    datadump = pickle.load(dbstore)
    dbstore.close()
sentences = []
itemData = {}
openebaydata()
for k, v in datadump.items():
    if v[12] == [0, 1]:
        v[12] = '3000'
    elif v[12] == [1, 0]:
        v[12] = '3000'
dbstore = open(dbfile, 'wb')
pickle.dump(datadump, dbstore)
dbstore.close()
openebaydata()
for k, v in datadump.items():
    try:
        v[13] = v[13]
        
    except:
        v.append([0, 1])
dbstore = open(dbfile, 'wb')
pickle.dump(datadump, dbstore)
dbstore.close()
openebaydata()
for k, v in datadump.items():
    itemData[k] = {}
    a = np.array(())
    v[0] = v[0].lower().split()
    for y in range(len(v[0])):
        try:
            b = model[v[0][y]]
        except:
            pass
            #print("word was not in vocabulary")
        a = np.hstack((a,b))
    changesize = 215 - a.size
    a = np.pad(a,(0, changesize), 'constant', constant_values = (0))
    itemData[k][0] = a
    itemData[k][1] = v[3]
    itemData[k][2] = v[5]
    itemData[k][3] = v[9]
    itemData[k][4] = v[12]
    itemData[k][5] = v[11]
    itemData[k][6] = [float(v[6]) + float(v[8])]
    itemData[k][7] = v[-1]
def convertonehot(y):
    index = preprocessing.LabelBinarizer()
    indexclasses = [itemData[k][y] for k,v in itemData.items()]
    index.fit(indexclasses)
    for k, v in itemData.items():
        itemData[k][y] = index.transform([itemData[k][y]]).tolist()

convertonehot(1)
convertonehot(2)
convertonehot(3)
convertonehot(4)
convertonehot(5)
featurelist = []
for k, v in itemData.items():
    datapoint = []
    features = []
    labels = []
    for y in v:
        if (y == 0):
            for x in v[y]:
                features.append(x)
        if (y == 1):
            for x in v[y]:
                for item in x:
                    features.append(item)
        if (y == 2):
            for x in v[y]:
                for item in x:
                    features.append(item)
        if (y == 3):
            for x in v[y]:
                for item in x:
                    features.append(item)
        if (y == 4):
            for x in v[y]:
                for item in x:
                    
                    features.append(item)
        if (y == 5):
            for x in v[y]:
                for item in x:
                    features.append(item)
        if (y == 6):
            for x in v[y]:
                features.append(x)
        if (y == 7):
            for x in v[y]:
                labels.append(x)
    datapoint.append(features)
    datapoint.append(labels)
    featurelist.append(datapoint)
listmultiplier1 = []
listmultiplier2 = []
listmultiplier3 = []
for x in featurelist:
    if x[1] == [0,1]:
        for z in range(3):
            y = deepcopy(x)
            y[0][-1] = y[0][-1]
            y[0][-1] = y[0][-1] + 50
            listmultiplier3.append(y)
for x in featurelist:
    if x[1] == [1,0]:
        q=[0, 0]
        for z in range(3):
            q = deepcopy(x)
            q[1] = [0,1]
            q[0][-1] = q[0][-1]
            q[0][-1] = q[0][-1] * 1.25**z
            listmultiplier2.append(q)
        
for x in featurelist:
    if x[1] == [1,0]:
        for z in range(3):
            p = deepcopy(x)
            p[0][-1] = p[0][-1]
            p[0][-1] = p[0][-1] * .75**z
            listmultiplier1.append(p)
for y in listmultiplier3:
    featurelist.append(y)
for p in listmultiplier1:
    featurelist.append(p)
for q in listmultiplier2:
    featurelist.append(q)

            

filteredfile ="processeddata2.pk1"
filteredstore = open(filteredfile, 'wb')
pickle.dump(featurelist, filteredstore)
filteredstore.close()
