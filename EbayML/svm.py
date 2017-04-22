import numpy as np
import pickle
import random
from sklearn.preprocessing import MinMaxScaler
from sklearn import svm
from sklearn.ensemble import AdaBoostClassifier
from random import shuffle
datafile = "processeddata.pk1"
datapoints = open(datafile, 'rb')
data = pickle.load(datapoints)
datapoints.close
featuresize = 271
interested = 0
notinterested = 0
for x in data:
    if x[1] == [1,0]:
        interested +=1
        x[1] = [1]
    if x[1] == [0,1]:
        notinterested +=1
        x[1] = [0]
shuffle(data)
batch_xs = np.array(data[0][0])
batch_xs2 = np.array(data[1][0])
batch_xs = np.vstack((batch_xs, batch_xs2))
batch_ys = np.array(data[0][1])
batch_ys2 = np.array(data[1][1])
batch_ys = np.vstack((batch_ys, batch_ys2))

for x in data[0:500]:
    batch_x = np.array(x[0])
    batch_xs = np.vstack((batch_xs, batch_x))
    batch_y = np.array(x[1])
    batch_ys = np.vstack((batch_ys, batch_y))
test_xs = np.array(data[0][0])
test_xs2 = np.array(data[1][0])
test_xs = np.vstack((test_xs, test_xs2))
test_ys = np.array(data[0][1])
test_ys2 = np.array(data[1][1])
test_ys = np.vstack((test_ys, test_ys2))
for x in data[-501:-1]:
    test_x = np.array(x[0])
    test_xs = np.vstack((test_xs, test_x))
    test_y = np.array(x[1])
    test_ys = np.vstack((test_ys, test_y))
print(interested)
print(notinterested)
print(x[1])
##x_scaler = MinMaxScaler()
##batch_xs = x_scaler.fit_transform(batch_xs)
##test_xs = x_scaler.fit_transform(test_xs)
clf = svm.SVC()
clf.fit(batch_xs, np.ravel(batch_ys))
accuracy = clf.score(test_xs, test_ys)
print(accuracy)
abc = AdaBoostClassifier(n_estimators = 5)
abc.fit(batch_xs, np.ravel(batch_ys))
accuracy = abc.score(test_xs, np.ravel(test_ys))
print(accuracy)
