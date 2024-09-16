# -*- coding: utf-8 -*-
import pandas as pd     #导入pandas库
import numpy as np      #导入nmypy库
import math             #导入数学函数模
import fun              #导入定义的函数
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
Z=np.zeros((len(A),13))
A_W0=A.iloc[0,1]  #第0个任务的维度
print(A_W0)
A_J0=A.iloc[0,2]  #第0个任务的经度
D2=np.zeros((len(B))) #预定义，第0个任务与所有会员之间的距离
for k in range(len(B)):
    B_Wk=B.iloc[k,1]   #第k个会员的维度
    B_Jk=B.iloc[k,2]   #第k个会员的经度
    d2=111.19*math.sqrt((A_W0-B_Wk)**2+(A_J0-B_Jk)**2*
       math.cos((A_W0+B_Wk)*math.pi/180)**2);
    D2[k]=d2
    
Z5=B.iloc[D2<=5,3].sum()
Z6=B.iloc[fun.find_I(6,30,6,30,D2,B),3].sum()
Z7=B.iloc[fun.find_I(6,33,6,45,D2,B),3].sum()
Z8=B.iloc[fun.find_I(6,48,7,3,D2,B),3].sum()
Z9=B.iloc[fun.find_I(7,6,7,21,D2,B),3].sum()
Z10=B.iloc[fun.find_I(7,24,7,39,D2,B),3].sum()
Z11=B.iloc[fun.find_I(7,42,7,57,D2,B),3].sum()
Z12=B.iloc[fun.find_I(8,0,8,0,D2,B),3].sum()

Z6_12=sum([Z6,Z7,Z8,Z9,Z10,Z11,Z12])
print('Z5= ',Z5)
print('sum(Z6~Z12)=',Z6_12)