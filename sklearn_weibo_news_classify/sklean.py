#coding: utf-8
import os 
import sys
import re
import jieba
import math
import random
#import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
from sklearn import metrics
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn.cluster import KMeans 
from sklearn import tree
class feature:
	def __init__(self,train_path,test_path):
		self.train_path = train_path
		self.test_path=test_path
		self.allClass = []
		self.stop=[]
		for (dirname,dirs,files) in os.walk(self.train_path):
			for eachdir in dirs:
				self.allClass.append(eachdir)

	def buildcorpus(self,pathh):
		corpus= []
		for eachclass in self.allClass:
			current_path = os.path.join(pathh,eachclass)
			for (dirname,dirs,filenames) in os.walk(current_path):
				for filename in filenames:
					with open(os.path.join(current_path,filename),'r') as f:
						content = f.read()
						corpus.append((content,eachclass))
		return corpus
	def train_and_test_data(self,corpus_train,corpus_test):
		train_data = [each[0] for each in corpus_train]
		train_target = [each[1] for each in corpus_train]
		test_data = [each[0] for each in corpus_test]
		test_target = [each[1] for each in corpus_test]
		return train_data, train_target, test_data, test_target

	def jieba_tokenizer(self,x):
		return jieba.cut(x)

	def calculate_result(self,pred,test):
			count=0
			for left,right in zip(pred,test_target):
				if left==right:
					count+=1
			return str(count/float(len(test_target)))
	def classifier(self,train_data,train_target,test_data,test_target):

		words_tfidf_vec = TfidfVectorizer(binary=False, tokenizer=self.jieba_tokenizer)
		train = words_tfidf_vec.fit_transform(train_data)
		test = words_tfidf_vec.transform(test_data)
		clf_svc = LinearSVC().fit(train, train_target)
		pred_svc=clf_svc.predict(test)
		#......................svm........................................
		clf_bayes=MultinomialNB().fit(train,train_target)
		pred_bayes=clf_bayes.predict(test)
		#.......................bayes......................................
		clf_knn=KNeighborsClassifier().fit(train,train_target)
		pred_knn=clf_knn.predict(test)
		#..........................knn......................................
		clf_tree=tree.DecisionTreeClassifier().fit(train,train_target)
		pred_tree=clf_tree.predict(test)
		#self.calculate_result(pred_kmeans.labels_,test_target)
		f=open('F:/classify/classify_content/result/result_sklearn.txt','w')
		f.write("sklearn分类器的分类结果为：")
		f.write("\n")
		f.write("svm分类器的分类结果为：")
		f.write(self.calculate_result(pred_svc,test_target))
		f.write("\n")
		f.write("Bayes分类器的分类结果为：")
		f.write(self.calculate_result(pred_bayes,test_target))
		f.write("\n")
		f.write("KNN分类器的分类结果为：")
		f.write(self.calculate_result(pred_knn,test_target))
		f.write("\n")
		f.write("决策树分类器的分类结果为：")
		f.write(self.calculate_result(pred_tree,test_target))
		f.write("\n")


#if __name__ == '__main__':
featureTest = feature('F:/classify/classify_content/data/ClassFile','F:/classify/classify_content/data/TestFile')
corpus_train=featureTest.buildcorpus('F:/classify/classify_content/data/ClassFile')
corpus_test=featureTest.buildcorpus('F:/classify/classify_content/data/TestFile')
train_data, train_target, test_data, test_target = featureTest.train_and_test_data(corpus_train,corpus_test)
featureTest.classifier(train_data, train_target, test_data, test_target)
