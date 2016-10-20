#!/usr/bin/python
# coding:utf-8 

import jieba
import os
import codecs
import sys
#reload(sys)
sys.getdefaultencoding()

word_num_pre_list = []
word_allClass_list = []

def cut_list():
	with open('F:/classify/stop.txt') as file_s:
		stopwordlist = file_s.readlines()
	for j in xrange(0, len(stopwordlist)):
		stopword = stopwordlist[j].strip()  #移除头尾的空格
		stopwordlist[j] = stopword
	return stopwordlist
def getWordDic(index,stopwordlist):
	index_word_fre = 0
	word_dic = {}

	file_path = 'F:/classify/classify_content/common/test_data/training/' + index 
	#file_list = os.listdir(file_path)
	for root, dirs, file_list in os.walk(file_path):
		for txtfile in file_list:
			final_path = root +'/'+ txtfile
			print final_path
			file_index_i = open(final_path,'r')
			text = file_index_i.read()
			text = "".join(text.split())  
			word_list = jieba.cut(text, cut_all = False) #采用精确模式
			#停用词表
			
			#便利每个样本文档的单词，若不在停用词表则记录
			for word in word_list:
				word = word.strip().encode('utf-8')

				if word in stopwordlist:
					pass
				else:
					index_word_fre = index_word_fre + 1
					if word in word_dic:
						word_dic[word] = word_dic[word] + 1 
					else:
						word_dic[word] = 1
						if word not in word_allClass_list:
							word_allClass_list.append(word)
	return word_dic, index_word_fre

def getWordFre(index,stopwordlist):
	(wordDic, index_word_pre) = getWordDic(index,stopwordlist)
	index_word_num = len(wordDic)
	print 'num = ' + str(index_word_num) + ',pre = '+ str(index_word_pre)
	word_num_pre_list.append(str(index_word_num))
	word_num_pre_list.append(str(index_word_pre))

	wordDicList = sorted(wordDic.iteritems(), key=lambda asd: asd[1], reverse=True)
	i_allwords_fre_path = 'F:/classify/classify_content/common/test_medfiles/fre/' + str(index) +'_fre.txt'
	file_i_allwords_fre = open(i_allwords_fre_path, 'w')
	for word_fre in wordDicList:
		#print word_fre[0] + 'worddic[0]'
		file_i_allwords_fre.write(word_fre[0]+','+str(word_fre[1])+'\n') #word_fre[0] 是每一类的特征词 word_fre[1]是出现次数
	file_i_allwords_fre.close

def fre(stopwordlist):
	path = 'F:/classify/classify_content/common/test_data/training/'
	index_list = os.listdir(path)
	for index in index_list:
		getWordFre(index,stopwordlist)
	file_word_num_allClass = open('F:/classify/classify_content/common/test_medfiles/word_num_allClass.txt','w')
	word_num_allClass = len(word_allClass_list)
	file_word_num_allClass.write(str(word_num_allClass)+'\n')
	print word_num_pre_list 
	for i in xrange(0,len(word_num_pre_list),2):
		file_word_num_allClass.write(word_num_pre_list[i]+','+word_num_pre_list[i+1]+'\n')
	file_word_num_allClass.close
	return index_list








