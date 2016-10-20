#coding: utf-8
import os
import sys
import re
import math
from numpy import *
import operator

class importTrain:
    def __init__(self,input_path,feature_file):
        self.input_path = input_path
        self.feature_file = feature_file
        featurepath = os.path.join(self.input_path, self.feature_file)
        f1 = open(featurepath ,'r')
        featureContent = f1.read().split('\n')
        feature = list()
        for eachfeature in featureContent:
            eachfeature = eachfeature.split(" ")
            if(len(eachfeature) == 1):
                feature.append(eachfeature[0])
        self.feature = list()
        for k in range(0,len(feature)-1):
            self.feature.append(feature[k])
        self.columncount = len(self.feature)
        #print self.columncount

    def importData(self,filename):
        datapath = self.input_path + filename
        f = open(datapath,'r')
        vectors = f.readlines()
        rowcount = len(vectors)
        returnMat = zeros((rowcount,self.columncount))
        class_label_vector = []
        index = 0
        for vector in vectors:
            vector = re.sub(r"{"," ",vector)
            vector = re.sub(r"\["," ",vector)
            vector = re.sub(r": ",":",vector)
            vector = re.sub(r"\'","",vector)
            vector = re.sub(r",","",vector)
            vector = re.sub(r"\]","",vector)          
            vector = vector.strip()
            each_vector_list = vector.split(' ')
            class_label_vector.append(each_vector_list[0])
            processing_data = []
            for i in xrange(1,len(each_vector_list)):                
                #print len(each_vector_list)
                each_data = re.search(r':(.+?)',each_vector_list[i])
                #each_data = re.sub(r"[\u4e00-\u9fa5]","",each_data)
                each_data = each_data.group()
                each_data = re.sub(r":","",each_data)
                processing_data.append(each_data)
            #print len(processing_data)
            returnMat[index, : ] = processing_data[:]
            index += 1
        if returnMat is not zeros:
            print True
        else:
            print False
        return returnMat,class_label_vector

    def Normalized(self,dataSet):
        minVals = dataSet.min(0)
        maxVals = dataSet.max(0)
        ranges = maxVals - minVals
        dataSet_norm = zeros(shape(dataSet))
        row = dataSet.shape[0]
        dataSet_norm = dataSet - tile(minVals,(row,1))
        dataSet_norm = dataSet_norm/tile(ranges,(row,1))
        return dataSet_norm 

    def classify(self,sample,dataSet,labels,k):
        dataSetSize=dataSet.shape[0]     #数据集行数即数据集记录数
        '''距离计算'''
        diffMat=tile(sample,(dataSetSize,1))-dataSet         #样本与原先所有样本的差值矩阵
        sqDiffMat=diffMat**2      #差值矩阵平方
        sqDistances=sqDiffMat.sum(axis=1)       #计算每一行上元素的和
        distances=sqDistances**0.5   #开方
        sortedDistIndicies=distances.argsort()      #按distances中元素进行升序排序后得到的对应下标的列表
        '''选择距离最小的k个点'''
        classCount={}
        for i in range(k):
            voteIlabel=labels[sortedDistIndicies[i]]
            classCount[voteIlabel]=classCount.get(voteIlabel,0) + 1
        '''从大到小排序'''
        sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        return sortedClassCount[0][0]

    def test(self,train_file,test_file,k,path):
        result_file=open(path,'w')
        (trainMat, trainClass) = self.importData('train.txt')
        (testMat,testClass) = self.importData('test.txt')
        #normTrainMat=self.Normalized(trainMat)
        #normTestMat = self.Normalized(testMat)
        rowSize = trainMat.shape[0]
        total = testMat.shape[0]
        errorCount = 0.0
        index = 0
        types={}
        result={}
        for vector in testMat:
            index += 1
            classifer_result = self.classify(vector,trainMat,trainClass,k)
            types[testClass[index-1]]=types.get(testClass[index-1],0)+1
            print("The classifier came back with: %s, the real answer is: %s" % (classifer_result, testClass[index-1]))
            if classifer_result != testClass[index-1]:
                result[testClass[index-1]]=result.get(testClass[index-1],0)+1
                errorCount +=1.0              
            else:
                errorCount = errorCount
        print("every types you duo shao")
        result_file.write('分类数据统计：')
        result_file.write('\n')
        for key in types:
            print key,types[key]
            result_file.write("类别："+key+" "+"数量："+str(types[key]))
            result_file.write('\n')
        result_file.write('\n')
        result_file.write("分类后的结果统计：")
        result_file.write('\n')
        for key in result:
            print("the class %s, error %s"%(key,result[key]))
            result_file.write("应该属于的类别："+key+" "+"被判为其他类别的数量为："+str(result[key]))
            result_file.write('\n') 
        result_file.write("错误率统计：")
        result_file.write('\n')
        result_file.write("错误率为："+str(errorCount/float(total)))
        result_file.write('\n')
        print("the total error rate is: %f" % (errorCount/float(total)))

     
#if __name__ == "__main__":
inputdata = importTrain('F:/classify/classify_content/result/','feature.txt')
path='F:/classify/classify_content/result/result.txt'
inputdata.test('train.txt','test.txt',8,path)
    