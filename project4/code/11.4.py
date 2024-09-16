# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#二值化处理
from PIL import Image
import numpy as np
import os
path='F:\\新教材资料\\水色图像水质评价\\图片'
d=os.listdir(path)               #图片文件夹下所有图像文件名
X=np.zeros((len(d),9))           #预定义自变量，即9个颜色矩特征指标
Y=np.zeros(len(d))               #预定义因变量
for i in range(len(d)):
  img = Image.open(path+'\\'+d[i]) #读取第i张图像
  im= img.split()                  #分离RGB颜色通道
  R=np.array(im[0])/255                #R通道
  row_1=int(R.shape[0]/2)-50
  row_2=int(R.shape[0]/2)+50
  con_1=int(R.shape[1]/2)-50
  con_2=int(R.shape[1]/2)+50
  R=R[row_1:row_2,con_1:con_2]
  G=np.array(im[1])/255                #G通道
  G=G[row_1:row_2,con_1:con_2]
  B=np.array(im[2])/255                #B通道
  B=B[row_1:row_2,con_1:con_2]
  # R,G,B一阶颜色矩
  r1=np.mean(R)
  g1=np.mean(G) 
  b1=np.mean(B)   
  # R,G,B二阶颜色矩
  r2=np.std(R)   
  g2=np.std(G)
  b2=np.std(B) 
  a=np.mean(abs(R - R.mean())**3)
  b=np.mean(abs(G - G.mean())**3)
  c=np.mean(abs(B - B.mean())**3)
  #R,G,B三阶颜色矩
  r3=a**(1./3) 
  g3=b**(1./3)    
  b3=c**(1./3)  
  #赋给预定义的自变量X
  X[i,0]=r1 
  X[i,1]=g1  
  X[i,2]=b1 
  X[i,3]=r2 
  X[i,4]=g2 
  X[i,5]=b2 
  X[i,6]=r3 
  X[i,7]=g3 
  X[i,8]=b3                                                                  
  
  #从图片文件名中，截取类别，构造因变量，赋给预定义的Y
  png_name=d[i]
  I=png_name.find('_',0,len(png_name))
  Y[i]=int(png_name[:I])

#按80%训练，20%测试，构建训练数据集和测试数据集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=4)

from sklearn.svm import SVC
clf = SVC(class_weight='balanced')#类标签平衡策略
clf.fit(x_train*40, y_train)
y1=clf.predict(x_test*40) #对测试数据进行预测，并获得预测结果
r=y1-y_test            #预测值与真实值相减
v=len(r[r==0])/len(y1)  #预测值与真实值相减为0，即预测准确，统计其准确率
print('预测准确率： ',v)
