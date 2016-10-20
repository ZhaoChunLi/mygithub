#coding: utf-8
import os
import jieba
import nltk
import pickle

class Train:
	def __init__(self):
		pass

	def get_data(self):
		folder_path ="F:\\classify\\classify_content\\bayes\\TrainFile"
		folder_list = os.listdir(folder_path)
		class_list = []
		#nClass = 0
		N = 200
		train_set = []
		test_set = []
		all_words = {}
		for class_name in folder_list:
			new_folder_path = folder_path + os.sep + class_name
			files = os.listdir(new_folder_path)
			class_list.append(class_name)
			j = 0
			nFile = min([len(files),N])
			for file in files:
				txt = open(new_folder_path + os.sep + file,'r')
				try:
					text = txt.read()
				except UnicodeDecodeError:
					pass
				word_cut = jieba.cut(text,cut_all = False)
				word_list = list(word_cut)
				for word in word_list:
					if word in all_words:
						all_words[word] += 1 
					else:
						all_words[word] = 1
				if j > 0.2*nFile:
					train_set.append((word_list,class_name))
				else:
					test_set.append((word_list,class_name))
				txt.close()
				j += 1
				print ('Folder',class_name,'-file-',file,'all_words length=',len(all_words))
		return train_set,test_set,all_words	

	def deal_data(self):
		(train_set,test_set,all_words) = Train.get_data(self)
		all_words_list = sorted(all_words.items(),key=lambda e:e[1],reverse=True)
		with open('F:\\classify\\classify_content\\bayes\\chinese_stopword.txt','r') as stopwords_file:
			stopwords_list = []
			for line in stopwords_list:
				stopwords_list.append(line[:len(line)-1])
			stopwords_file.close()
		print stopwords_list
		print 'stop'
		all_words_list_copy = []
		for word in all_words_list:
			if word[0].encode("utf-8") not in stopwords_list:
				all_words_list_copy.append(word)
		all_words_list = all_words_list_copy[:]
		return all_words_list

	def words_dict(self):
		all_words_list = Train.deal_data(self)
		word_features = []
		for word in all_words_list:
			word_features.append(word[0])
		return word_features

	def document_features(self,document):
		document_words = set(document)
		features = {}
		for word in word_features:
			features['contains(%s)'%word] = (word in document_words)
		return features

	def text_classifier(self):
		(train_set,test_set,all_words) = Train.get_data(self)
		train_data = [(Train.document_features(self,d),c) for (d,c) in train_set]
		print('train number', len(train_set), "\n",'test number', len(test_set))
		#nltk朴素贝叶斯分类器
		print('Training...')
		classifier = nltk.NaiveBayesClassifier.train(train_data)
		del train_data
		print('Testing...')
		test_data = [(Train.document_features(self,d), c) for (d,c) in test_set]
		test_error = nltk.classify.accuracy(classifier, test_data)
		with open('F:\\classify\\classify_content\\bayes\\.cache_file', 'wb') as cache_file:
			pickle.dump(classifier, cache_file)
			pickle.dump(word_features, cache_file)
			cache_file.close()
		return test_error

#if __name__ == '__main__':
bayes_train = Train()
word_features = bayes_train.words_dict()
accuracy = bayes_train.text_classifier()
print ('test accuracy:' , accuracy) 
