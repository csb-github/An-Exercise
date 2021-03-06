from collections import Counter
import numpy as np
import os
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import confusion_matrix

def make_dictionary(train_dir):
    emails=[os.path.join(train_dir,f) for f in os.listdir(train _dir)]
    all_words=[]
    for email in emails:
        with open(email) as m:
            for i,line in enumerate(m):
                if i==2:
                    words=line.split()
                    all_words+=words
    dictionary=Counter(all_words)
    list_to_remove=dictionary.keys()
    for item in list_to_remove:
        if isalpha(item) == Flase:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary=dictionary.most_common(3000)
    return dictionary
 
def extract_features(train_dir):
    files=[os.path.join(train_dir,f) for f in os.listdir(train_dir)]
    feature_matrix=np.zeros(len(files),3000))
    docID=0
    for file in files:
        with open(file) as fi:
            for i,line in enumerate(fi):
                if i==2:
                    words = line.split()
                    for word in words:
                        wordID=0
                        for i,d in enumerate(dictionary):
                            if d[0] == word:
                                wordID=i
                                feature_matrix[docID,wordID]=words.count(word)
            docID=docID+1
    return features_matrix

train_dir='train-mails'
dictionary=make_dictionary(train_dir)
train_labels=np.zeros(702)
train_labels[351:701]=1
train_matrix=extract_features(train_dir)

model1=MultinomialNB()
model2=LinearSVC()
model1.fit(train_matrix,train_labels)
model2.fit(train_matrix,train_labels)

test_dir='test-mails'
test_matrix=extract_features(test_dir)
test_labels=np.zeros(260)
test_labels[130:260]=1
results1=model1.predict(test_matrix)
results2=model2.predict(test_matrix)
print(confusion_matrix(test_labels,predict1))
print(confusion_matrix(test_labels,predict2))
