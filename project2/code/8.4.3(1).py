# -*- coding: utf-8 -*-
'''
import pandas as pd      #导入pandas库
import math               #导入数学函数包
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
A_W0=A.iloc[0,1]  #第0个任务的维度
A_J0=A.iloc[0,2]  #第0个任务的经度
A_W1=A.iloc[1,1]  #第1个任务的维度
A_J1=A.iloc[1,2]  #第1个任务的经度
B_W0=B.iloc[0,1]  #第0个会员的维度
B_J0=B.iloc[0,2]  #第0个会员的经度
#第0个任务到第1个任务之间的距离
d1=111.19*math.sqrt((A_W0-A_W1)**2+(A_J0-A_J1)**2*
math.cos((A_W0+A_W1)*math.pi/180)**2);  
#第0个任务到第0个会员之间的距离
d2=111.19*math.sqrt((A_W0-B_W0)**2+(A_J0-B_J0)**2*
   math.cos((A_W0+B_W0)*math.pi/180)**2);
print('d1= ',d1)
print('d2= ',d2)
'''
'''
import pandas as pd     #导入pandas库
import numpy as np      #导入numpy库
import math               #导入数学函数库
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
A_W0=A.iloc[0,1]  #第0个任务的维度
A_J0=A.iloc[0,2]  #第0个任务的经度
# 预定义数组D1,用于存放第0个任务与所有任务之间的距离
# 预定义数组D2,用于存放第0个任务与所有会员之间的距离
D1=np.zeros((len(A)))
D2=np.zeros((len(B)))
for t in range(len(A)):
     A_Wt=A.iloc[t,1]  #第t个任务的维度
     A_Jt=A.iloc[t,2]  #第t个任务的经度
     #第0个任务到第t个任务之间的距离
     dt=111.19*math.sqrt((A_W0-A_Wt)**2+(A_J0-A_Jt)**2*
       math.cos((A_W0+A_Wt)*math.pi/180)**2);  
     D1[t]=dt
for k in range(len(B)):
     B_Wk=B.iloc[k,1] #第k个会员的维度
     B_Jk=B.iloc[k,2] #第k个会员的经度
     #第0个任务到第k个会员之间的距离
     dk=111.19*math.sqrt((A_W0-B_Wk)**2+(A_J0-B_Jk)**2*
         math.cos((A_W0+B_Wk)*math.pi/180)**2); 
     D2[k]=dk
'''
'''
import pandas as pd      #导入pandas库
import numpy as np       #导入numpy库
import math               #导入数学函数包
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
A_W0=A.iloc[0,1]  #第0个任务的维度
A_J0=A.iloc[0,2]  #第0个任务的经度
# 预定义数组D1,用于存放第0个任务与所有任务之间的距离
# 预定义数组D2,用于存放第0个任务与所有会员之间的距离
D1=np.zeros((len(A)))
D2=np.zeros((len(B)))
for t in range(len(A)):
    A_Wt=A.iloc[t,1]  #第t个任务的维度
    A_Jt=A.iloc[t,2]  #第t个任务的经度
    #第0个任务到第t个任务之间的距离
    dt=111.19*math.sqrt((A_W0-A_Wt)**2+(A_J0-A_Jt)**2*
       math.cos((A_W0+A_Wt)*math.pi/180)**2);  
    D1[t]=dt
for k in range(len(B)):
    B_Wk=B.iloc[k,1]          #第k个会员的维度
    B_Jk=B.iloc[k,2]  #第k个会员的经度
    #第0个任务到第k个会员之间的距离
    dk=111.19*math.sqrt((A_W0-B_Wk)**2+(A_J0-B_Jk)**2*
        math.cos((A_W0+B_Wk)*math.pi/180)**2); 
    D2[k]=dk
Z1=len(D1[D1<=5]) 
Z2=A.iloc[D1<=5,3].mean()
Z3=len(D2[D2<=5])   
Z4=B.iloc[D2<=5,5].mean()
Z5=B.iloc[D2<=5,3].sum()
print('Z1= ',Z1)
print('Z2= ',Z2)
print('Z3= ',Z3)
print('Z4= ',Z4)
print('Z5= ',Z5)
'''

import pandas as pd     #导入pandas库
import numpy as np      #导入numpy库
import math               #导入数学函数包
A=pd.read_excel('附件一：已结束项目任务数据.xls') 
B=pd.read_excel('附件二：会员信息数据.xlsx')
# 预定义,存放所有任务的指标Z1、Z2、Z3、Z4、Z5
Z=np.zeros((len(A),6))
for t in range(len(A)):
    A_Wt=A.iloc[t,1]  #第q个任务的维度
    A_Jt=A.iloc[t,2]  #第q个任务的经度
    # 预定义数组D1,用于存放第q个任务与所有任务之间的距离
    # 预定义数组D2,用于存放第q个任务与所有会员之间的距离
    D1=np.zeros((len(A)))
    D2=np.zeros((len(B)))
    for i in range(len(A)):
       A_Wi=A.iloc[i,1]  #第t个任务的维度
       A_Ji=A.iloc[i,2]  #第t个任务的经度
       #第q个任务到第t个任务之间的距离
       d1=111.19*math.sqrt((A_Wt-A_Wi)**2+(A_Jt-A_Ji)**2*
          math.cos((A_Wt+A_Wi)*math.pi/180)**2);  
       D1[i]=d1
    for k in range(len(B)):
       B_Wk=B.iloc[k,1]          #第k个会员的维度
       B_Jk=B.iloc[k,2]  #第k个会员的经度
       #第q个任务到第k个会员之间的距离
       d2=111.19*math.sqrt((A_Wt-B_Wk)**2+(A_Jt-B_Jk)**2*
          math.cos((A_Wt+B_Wk)*math.pi/180)**2); 
       D2[k]=d2
    Z[t,0]=t
    Z[t,1]=len(D1[D1<=5])
    Z[t,2]=A.iloc[D1<=5,3].mean()
    Z[t,3]=len(D2[D2<=5])
    Z[t,4]=B.iloc[D2<=5,5].mean()
    Z[t,5]=B.iloc[D2<=5,3].sum()



