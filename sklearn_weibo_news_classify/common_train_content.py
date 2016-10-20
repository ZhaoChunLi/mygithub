#!/usr/bin/python
# coding:utf-8 
from test_fre_content import*

def training(index,i):
	print 'training:' + str(index)
	word_num_allClass_path = 'F:/classify/classify_content/common/test_medfiles/word_num_allClass.txt'
	file_word_num_allClass = open(word_num_allClass_path,'r')
	info_list = file_word_num_allClass.readlines()
	#所有类中的不同单词个数
	word_num_allClass = int(info_list[0].strip())
	print word_num_allClass
	index_word_num_pre = info_list[i].strip().split(',')
	print index_word_num_pre 
	index_word_pre = int(index_word_num_pre[1])

    #读入类别index的文件
	index_file_path = 'F:/classify/classify_content/common/test_medfiles/fre/' + index+ '_fre.txt'
	file_index = open(index_file_path,'r')
	word_fre_list = file_index.readlines()

	word_p_dic={}
	for word_fre in word_fre_list:
		word_fre = word_fre.strip().split(',')
		#print word_fre[0] 
		word = word_fre[0]
		fre_ = int(word_fre[1])
		p_index_word = float(fre_ +1)/(index_word_pre)
		word_p_dic[word] = p_index_word

    #排序
	dic_list = sorted(word_p_dic.iteritems(), key=lambda asd: asd[1], reverse=True)
	outcome_file_path = 'F:/classify/classify_content/common/common_training_outcome/' + index + '_bayestraining.txt'
	file_outcome = open(outcome_file_path, 'w')
    #第一行写入所有单词个数 以及 单词词频和
	file_outcome.write(str(word_num_allClass) + ',' + str(index_word_pre) + '\n')
	j = 0
	for word_p in dic_list:
		file_outcome.write(word_p[0] + ',' +str(word_p[1])+'\n')
		j = j+1
	file_outcome.close

stopwordlist=cut_list()
index_list = fre(stopwordlist)
for index in index_list:
	i=index_list.index(index) + 1
	training(index,i)

