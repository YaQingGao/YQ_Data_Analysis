# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:33:38 2019

@author: lenovo
"""
import numpy as np 
import pandas as pd
Z=np.load('Z.npy')
Data=pd.DataFrame(Z[:,1:])
Data=Data.fillna(0)
R=Data.corr()

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data=Data.as_matrix() #数据框转化为数组形式
scaler.fit(data) 
data=scaler.transform(data)  

from sklearn.decomposition import PCA
pca=PCA(n_components=0.9) #累计贡献率提取90%以上
pca.fit(data)
x=pca.transform(data)  #返回主成分
tzxl=pca.components_    #特征向量          
tz=pca.explained_variance_      #特征值   
gxl=pca.explained_variance_ratio_  #累计贡献率

#线性回归
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
A4=A.iloc[:,4].values
x_0=x[A4==0,:] #未执行任务主成分数据
x_1=x[A4==1,:] #执行任务主成分数据
y=A.iloc[:,3].values
y=y.reshape(len(y),1)
y_0=y[A4==0]#未执行任务定价数据
y_1=y[A4==1]#执行任务定价数据



from sklearn.linear_model import LinearRegression as LR
lr = LR()    #创建线性回归模型类
lr.fit(x_1, y_1) #拟合
Slr=lr.score(x_1,y_1)   # 判定系数 R^2
c_x=lr.coef_        # x对应的回归系数
c_b=lr.intercept_   # 回归系数常数项
print('判定系数： ',Slr)



from sklearn.neural_network import MLPRegressor 
#两个隐含层300*5
clf = MLPRegressor(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(300,5), random_state=1) 
clf.fit(x_1, y_1);   
rv1=clf.score(x_1,y_1)
y_0r=clf.predict(x_0)
print('拟合优度： ',rv1)

xx=pd.concat((Data,A.iloc[:,[3]]),axis=1) #12个指标+任务定价，自变量
xx=xx.as_matrix()                         #转化为数组
yy=A4.reshape(len(A4),1)                  #任务执行情况，因变量
#对自变量与因变量按训练80%、测试20%随机拆分
from sklearn.model_selection import train_test_split
xx_train, xx_test, yy_train, yy_test = train_test_split(xx, yy, test_size=0.2, random_state=4)

from sklearn import svm
#用高斯核，训练数据类别标签作平衡策略
clf = svm.SVC(kernel='rbf',class_weight='balanced')  
clf.fit(xx_train, yy_train) 
rv2=clf.score(xx_train, yy_train);#模型准确率
yy1=clf.predict(xx_test)
yy1=yy1.reshape(len(yy1),1)
r=yy_test-yy1
rv3=len(r[r==0])/len(r) #预测准确率
print('模型准确率： ',rv2)
print('预测准确率： ',rv3)
xx_0=np.hstack((Z[A4==0,1:],y_0r.reshape(len(y_0r),1)))#预测自变量
P=clf.predict(xx_0)   #预测结果，1-执行，0-未被执行
R1=len(P[P==1])      #预测被执行的个数
R1=int(R1*rv3)       #任务完成增加量
print('任务完成增加量： ',R1)
R2=sum(y_0r)-sum(y_0)   #成本增加额
print('成本增加额： ',R2)
