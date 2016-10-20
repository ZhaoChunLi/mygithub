
from numpy import *
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)   #caculate mean of each col
    meanRemoved = dataMat - meanVals   #remove mean
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)                      #index, sort goes smallest to largest
    #print eigValInd
    eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
    redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
    lowDDataMat = meanRemoved * redEigVects   #transform data into new dimensions
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def plot2(dataSet1,y,dataSet2):
    dataArr1 = array(dataSet1)
    dataArr2 = array(dataSet2)
    n = shape(dataArr1)[0]
    n1=shape(dataArr2)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    xcord3=[];ycord3=[]
    j=0
    for i in range(n):
        xcord1.append(dataArr1[i,0]); ycord1.append(dataArr1[i,1])
        xcord2.append(dataArr2[i,0]); ycord2.append(dataArr2[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(len(y)):
        if y[i]==1:
            ax.scatter(real(xcord1[i]), real(ycord1[i]), s=30, c='red', marker='s')
        else:
            ax.scatter(real(xcord1[i]), real(ycord1[i]), s=30, c='green', marker='s')
    #ax.scatter(xcord2, ycord2, s=30, c='blue')

    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()

def plot3(dataSet1,y):
    dataArr1 = array(dataSet1)
    n = shape(dataArr1)[0]
    xcord1 = []
    ycord1 = []
    zcord1 = []
    j = 0
    for i in range(n):
        xcord1.append(dataArr1[i, 0])
        ycord1.append(dataArr1[i, 1])
        zcord1.append(dataArr1[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    for i in range(n):
        if (y[i]==1):
            ax.scatter(xcord1[i], ycord1[i],zcord1[i], c='y')
        else:
            ax.scatter(xcord1[i], ycord1[i],zcord1[i], c='r')
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()

if __name__=='__main__':
     #mata=loadDataSet('/Users/hakuri/Desktop/testSet.txt')
     #a,b= pca(mata, 2)
     #plotBestFit(a,b)
     data=np.array([[1, -1], [1, 1]])
     w, v = linalg.eig(data)
     print v
     print v*v.T
     print data*v*v.T
