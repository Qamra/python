import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#简单实施KNN
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]   #取出dataSet的shape
    diffMat = np.tile(inX,(dataSetSize,1)) - dataSet    #tile()将inX转换成与dataSet相同形状的数组
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()  #argsort()函数用法：从小到大排序，取其索引值index输出
    #print(sortedDistIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #print(classCount)
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse=True)  #key=operator.itemgetter(1)意思是使用字典的第二个元素排序
    return sortedClassCount[0][0]

#从文本文件中解析数据
def file2matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()   #readlines()读取文件所有行，存储在一个list中，每行作为一个元素
    numberOfLines = len(arrayOLines)   #读取文件中元素数
    returnMat = np.zeros((numberOfLines,3))
    classLabelVextor = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVextor.append(int(listFromLine[-1]))
        index += 1
    return returnMat,classLabelVextor

#数据集归一化
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals,(m,1))
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    return normDataSet,ranges,minVals
