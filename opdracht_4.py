import skimage
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import numpy as np
import random

digits = datasets.load_digits()
print(digits.data)
print(digits.target)

clf = svm.SVC(gamma=0.001, C=100)

# get random indexes
potential_indexes = list(range(len(digits.data)))
train_indexes = random.sample(potential_indexes, k = int(len(digits.data) *2/3))
test_indexes = [index for index in potential_indexes if index not in train_indexes]

#get the data en targets for the test en train
train_data = [ digits.data[i] for i in train_indexes]
train_target = [ digits.target[i] for i in train_indexes]

test_data = [ digits.data[i] for i in test_indexes]
test_target = [ digits.target[i] for i in test_indexes]


#train
X,y = train_data, train_target
clf.fit(X,y)

#check accuracy
correct = 0
for items in range(len(test_data)):
    if clf.predict(test_data[items:items+1]) == test_target[items]:
        correct +=1
print("The accuracy is: ", str(correct / len(test_data) * 100), "%")
