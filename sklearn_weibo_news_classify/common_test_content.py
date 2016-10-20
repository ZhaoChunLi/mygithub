#!usr/bin/python
# coding:utf-8 
import os
import math
import jieba
import sys

#ABSPATH = os.path.abspath(sys,argv[0]) #返回绝对路径
#ABSPATH = os.path.dirname(ABSPATH) + '/'
#ABSPATH = 'D:/Project/classifier python/test_bayes/'

def getPofClass(index,word_list):
	#输入类index的贝叶斯训练结果文件
	index_training_path ='F:/classify/classify_content/common/common_training_outcome' +'/'+ index + '_bayestraining.txt'
	file_index_training = open(index_training_path,'r')
	dic_training = {}
	training_word_p_list = file_index_training.readlines()
	allwords_fre_allwords_num = training_word_p_list[0].strip() 
	allwords_fre = int(allwords_fre_allwords_num[1])
	allwords_num = int(allwords_fre_allwords_num[0])
	for i in xrange(1, len(training_word_p_list)):
		word_p = training_word_p_list[i].strip().split(',')
		dic_training[word_p[0]] = float(word_p[1])

	#遍历测试样本的wordlist,求每个word的p
	p_list = []
	for word in word_list:
		word = word.strip()
		if word in dic_training:
			p_list.append(str(dic_training[word]))
		else:
			p_list.append(str(1.0))

	#计算P
	p_index = 0
	for p in p_list:
		p = math.log(float(p),2)
		p_index = p_index + p
		#print p_index
	#print p_index
	return -p_index

def list_cut():
	stopword_path = 'F:/classify/stop.txt'
	with open(stopword_path) as file_stopword:
		stopword_list = file_stopword.readlines()
	for i in xrange(0, len(stopword_list)):
		word = stopword_list[i].strip()
		stopword_list[i] = word
	return stopword_list
def common_cut(text,stopword_list):
	#分词
    text = "".join(text.split())
    word_list = jieba.cut(text, cut_all=False)
    #去停用词
    word_list_nostop = []
    for word in word_list:
        word = word.strip().encode('utf-8')
        if word in stopword_list:
            pass
        else:
            word_list_nostop.append(word)
    
    #求每个类index的P
    max = 0
    maxIndex = 0
    dir_path = 'F:/classify/classify_content/common/test_data/test/'
    file_list = os.listdir(dir_path)
    for index in file_list:
    	#print index
    	y = getPofClass(index,word_list_nostop)
    	if y !=float("inf") and y > float(max):
    		max = y
    		maxIndex = index
    return maxIndex

#从本地文件获取文本内容
def getTextFromNative(index):
	test_file_path = 'F:/classify/classify_content/common/test_data/test/' +index
	text_list=[]
	for root,dirs,txt_list in os.walk(test_file_path):
		for txtfile in txt_list:
			final_txt_path = root + '/' +txtfile
			file_test = open(final_txt_path, 'r')
			text = file_test.read()
			text_list.append(text)
	return txt_list,text_list

#测试本地文件
def nativeTest(path,stopword_list):
	dir_path = 'F:/classify/classify_content/common/test_data/test/'
	file_list = os.listdir(dir_path)
	all_count = 0
	count=0
	all_right_count=0
	types={}
	error={}
	for index in file_list:
		(txt_list,text_list) = getTextFromNative(index)
		all_count = len(txt_list)
		for i in xrange(0, all_count):
			getIndex = common_cut(text_list[i],stopword_list)
			if getIndex == index:
				types[index]=types.get(index,0)+1;
				print txt_list[i] 
				print '该新闻属于：' + getIndex + '类' + '---分类正确' 
				all_right_count = all_right_count + 1
				count+=1;
			else:
				count+=1;
				error[index]=error.get(index,0)+1;
				types[index]=types.get(index,0)+1;
				print txt_list[i] 
				print '该新闻属于：' + getIndex + '类' + '---分类错误'
		#rate_outcome = open(ABSPATH + 'outcome/rate.txt', 'w')
		#rate_outcome.write(str(right_count) / str(all_count))
	f=open(path,'w+')
	f.write('分类前数量统计：')
	f.write('\n')
	for type in types:
		f.write('类别%s的数量为%s'%(type,str(types[type])))
		f.write('\n')
	f.write('\n')
	f.write('分类结果数据统计：')
	f.write('\n')
	for err in error:
		f.write('类别%s中判别错误的数量为%s'%(err,str(error[err])))
		f.write('\n')
		rate=float(error[err])/float(types[err])
		f.write('错误率为：%s'%(str(rate)))
		f.write('\n')
	f.write('\n')
	all_rate=float(count-all_right_count)/float(count)
	f.write('总体错误率为：%s'%(str(all_rate)))
		
path='F:/classify/classify_content/common/result.txt'
stopword_list=list_cut()
nativeTest(path,stopword_list)



