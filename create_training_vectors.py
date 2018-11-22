from sklearn import preprocessing, svm
from sklearn.pipeline import Pipeline
import nltk
import numpy
import subprocess
import time
import utility
import json
import csv
import unicodedata
import sys
reload(sys)
sys.setdefaultencoding('utf8')
##############################################################
p1=0
n1=0
svm_module = svm.SVC()
classifier = Pipeline(steps= [('svm', svm_module)]) #[('scale', scaler), ('svm', svm_module)])


def create_classifier():
    global classifier
    positive = numpy.loadtxt("training/positive.csv", delimiter=',')
    negetive = numpy.loadtxt("training/negative.csv", delimiter=',')
    X = numpy.concatenate((positive, negetive), axis=0)
    p = numpy.ones((p1, 1))
    n = numpy.full((n1, 1), -1, dtype=numpy.int64)
    Y = numpy.concatenate((p, n), axis=0)
    y = Y.ravel()
    # scale
    scaler = preprocessing.StandardScaler().fit(X)
    classifier.fit(X, y)


#code for creating dataset from data line 1 to k and n to end
def create_training_set(k, n):
    file1 = open('data.jsonl', 'r')
    file2 = open('training/positive.csv', 'w')
    file3 = open('training/negative.csv', 'w')


    i=1
    global p1,n1
    while i<=2459:
        if i<k or i>=n :

            #for line in file1.readline():
            str=json.loads(file1.readline())
            #print str['postText'][0]
            stringsr=str['postText'][0]
            #creating title vector
            title_vector=numpy.array(utility.create_vector(stringsr))

            wr1 = csv.writer(file2)
            wr2 = csv.writer(file3)
            if str['truthClass']=="clickbait":

                wr1.writerow(title_vector)
                p1+=1
             #   print p1
            if str['truthClass'] == "no-clickbait":
                wr2.writerow(title_vector)
              #  print n1
                n1+=1
        i+=1
    file2.close()
    file1.close()
    file3.close()


def find_accuracy(k,n):
    file5=open('data.jsonl','r')
    i=1
    total=0
    right=0
    while i<=2459:
        if i>=k and i<n:
            line=file5.readline()
            data=json.loads(line)
            title_vector = numpy.array(utility.create_vector(data['postText'][0])).reshape(1, -1)
            prediction = classifier.predict(title_vector)
            if prediction[0] == 1 and data['truthClass']=="clickbait":
                right+=1
                #print i,
                #print "   1"
            if prediction[0] != 1 and data['truthClass'] == "no-clickbait":
                right+=1
                #print i,
                #print "   0"
            total+=1

        i+=1
    print right
    print total
    accuracy=float(right)/total
    print accuracy
    print p1
    print n1
    file5.close()

if __name__ == '__main__':
    k=1475
    n=1968
    create_training_set(k, n)
    create_classifier()
    find_accuracy(k,n)
