#coding:utf-8
import pickle
import jieba
import nltk
import os
import re

class Test:
    def __init__(self,input_path):
        self.input_path = input_path
        self.folder = []
        for (dirname,dirs,files) in os.walk(self.input_path):
            for eachdir in dirs:
                self.folder.append(os.path.join(dirname,eachdir))

    def document_features(self,document):
        document_words = set(document) #文件中所有词的集合
        features = {}
        (classifier,word_features)= Test.read_cache(self)
        for word in word_features:
            features['contains(%s)'%word] = (word in document_words)
        return features
        

    def read_cache(self):
        with open('F:\\classify\\classify_content\\bayes\\.cache_file','rb') as cache_file:
            classifier = pickle.load(cache_file)
            word_features = pickle.load(cache_file)
            cache_file.close()
        print word_features
        print "nishishenme"
        print classifier
        print "nine"
        return classifier,word_features

    def classify(self,path):
        classify_result = {}
        (classifier,word_features)= Test.read_cache(self)
        f=open(path,'w+')
        for folder in self.folder:
            correct = 0
            error = 0
            for file in os.listdir(folder):
                total = 0
                txt = open(folder + os.sep + file,'r')
                try:
                    text = txt.read()
                except UnicodeDecodeError:
                    pass
                txt.close()
                word_cut = jieba.cut(text, cut_all = False)
                word_list = list(word_cut)
                user_test_data = Test.document_features(self,word_list)
                classified = classifier.classify(user_test_data)
                classify_result[file] = classified
                cur_class = re.sub(r'F:\\classify\\classify_content\\bayes\\TestFile\\','',folder)
                if classified != cur_class:
                    error += 1
                else:
                    correct +=1
                print (cur_class,file,'is classifed to', classified)
            rate = float(correct)/ float(error + correct)
            f.write('分类结果数据统计：')
            f.write('\n')
            f.write('实际类'+cur_class+'共有'+str(error + correct)+'个')
            f.write('\n')
            f.write('其中正确分类的有'+str(correct)+'个')
            f.write('\n')
            f.write('其中错误分类的有'+str(error)+'个')
            f.write('\n')
            f.write('正确率为：'+str(rate))
            f.write('\n')
            f.write('\n')
            print rate

#if __name__ == '__main__':
bayes_test = Test("F:\\classify\\classify_content\\bayes\\TestFile")
path='F:\\classify\\classify_content\\bayes\\result.txt'
bayes_test.classify(path)