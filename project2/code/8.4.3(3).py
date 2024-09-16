# -*- coding: utf-8 -*-
import pandas as pd     #导入pandas库
import numpy as np      #导入nmypy库
import math             #导入数学函数模
import fun              #导入定义的函数

A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
Z=np.zeros((len(A),13))
for t in range(len(A)):
   A_Wt=A.iloc[t,1]  #第t个任务的维度
   A_Jt=A.iloc[t,2]  #第t个任务的经度
   D1=np.zeros(len(A))
   D2=np.zeros(len(B))
   for i in range(len(A)):
      A_Wi=A.iloc[i,1]  #第i个任务的维度
      A_Ji=A.iloc[i,2]  #第i个任务的经度
      d1=111.19*math.sqrt((A_Wt-A_Wi)**2+(A_Jt-A_Ji)**2*
         math.cos((A_Wt+A_Wi)*math.pi/180)**2);  
      D1[i]=d1
   for k in range(len(B)):
      B_Wk=B.iloc[k,1]   #第k个会员的维度
      B_Jk=B.iloc[k,2]   #第k个会员的经度
      d2=111.19*math.sqrt((A_Wt-B_Wk)**2+(A_Jt-B_Jk)**2*
         math.cos((A_Wt+B_Wk)*math.pi/180)**2);
      D2[k]=d2

   Z[t,0]=t
   Z[t,1]=len(D1[D1<=5])
   Z[t,2]=A.iloc[D1<=5,3].mean()
   Z[t,3]=len(D2[D2<=5])
   Z[t,4]=B.iloc[D2<=5,5].mean()
   Z[t,5]=B.iloc[D2<=5,3].sum()
   Z[t,6]=B.iloc[fun.find_I(6,30,6,30,D2,B),3].sum()
   Z[t,7]=B.iloc[fun.find_I(6,33,6,45,D2,B),3].sum()
   Z[t,8]=B.iloc[fun.find_I(6,48,7,3,D2,B),3].sum()
   Z[t,9]=B.iloc[fun.find_I(7,6,7,21,D2,B),3].sum()
   Z[t,10]=B.iloc[fun.find_I(7,24,7,39,D2,B),3].sum()
   Z[t,11]=B.iloc[fun.find_I(7,42,7,57,D2,B),3].sum()
   Z[t,12]=B.iloc[fun.find_I(8,0,8,0,D2,B),3].sum()
np.save('Z',Z)