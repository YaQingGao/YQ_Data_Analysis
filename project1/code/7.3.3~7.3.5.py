# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:53:57 2018

@author: Administrator
"""
import pandas as pd
data=pd.read_excel('Data.xlsx')
data=data[data>0]
data=data.dropna()
from sklearn.preprocessing import StandardScaler  
X=data.iloc[:,1:]
scaler = StandardScaler()
scaler.fit(X) 
X=scaler.transform(X)  
from sklearn.decomposition import PCA 
pca=PCA(n_components=0.95)      #累计贡献率为95%
Y=pca.fit_transform(X)            #满足累计贡献率为95%的主成分数据
gxl=pca.explained_variance_ratio_   #贡献率
import numpy as np
F=np.zeros((len(Y)))
for i in range(len(gxl)):
    f=Y[:,i]*gxl[i]
    F=F+f
    
fs1=pd.Series(F,index=data['ts_code'].values)
Fscore1=fs1.sort_values(ascending=False)   #降序，True为升序
    
stk=pd.read_excel('stkcode.xlsx')
stk=pd.Series(stk['name'].values,index=stk['ts_code'].values)
stk1=stk[data['ts_code'].values]
fs2=pd.Series(F,index=stk1.values)
Fscore2=fs2.sort_values(ascending=False)   #降序，True为升序


