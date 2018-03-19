import kNN
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

group,labels = kNN.createDataSet()
print('group = ',group,'\n','labels = ',labels)

#判断分类
print(kNN.classify0([0,0],group,labels,3))

#k-紧邻实例1：约会网站
datingDataMat,datingLabels = kNN.file2matrix('datingTestSet2.txt')
print(datingDataMat,'\n',datingLabels)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,0],datingDataMat[:,1],15.0*np.array(datingLabels),15.0*np.array(datingLabels))
plt.show()

#数据集归一化
normMat,ranges,minVals = kNN.autoNorm(datingDataMat)
print(normMat)