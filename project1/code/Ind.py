# 计算简单算术移动平均线MA 
import pandas as pd
def MA(data,N1,N2,N3):
   MAN1=pd.rolling_mean(data['close'].values,N1) 
   MAN2=pd.rolling_mean(data['close'].values,N2) 
   MAN3=pd.rolling_mean(data['close'].values,N3) 
   return (MAN1,MAN2,MAN3)
   
# 计算指数平滑移动平均线EMA
def MACD(data): 
    import numpy as np 
    EMA12 = pd.ewma(data['close'].values, 12)
    EMA26 = pd.ewma(data['close'].values, 26)
    DIF=EMA12- EMA26
    DEA=np.zeros((len(DIF)))
    MACD=np.zeros((len(DIF)))
    for t in range(len(DIF)):
        if t==0:
             DEA[t]= DIF[t]
        if t>0:
             DEA[t]=(2*DIF[t]+8*DEA[t-1])/10
        MACD[t]=2*(DIF[t]-DEA[t])
    return MACD

#计算随机指标KDJ
def KDJ(data,N):
    import numpy as np 
    Lmin=pd.rolling_min(data['low'].values,N)
    Lmax=pd.rolling_max(data['high'].values,N)
    RSV=(data['close'].values-Lmin)/(Lmax-Lmin)
    K=np.zeros((len(RSV)))
    D=np.zeros((len(RSV)))
    J=np.zeros((len(RSV)))
    for t in range(N,len(data)):
        if t==0:
            K[t]=RSV[t]
            D[t]=RSV[t]
        if t>0:
            K[t]=2/3*K[t-1]+1/3*RSV[t]
            D[t]=2/3*D[t-1]+1/3*K[t]
        J[t]=3*D[t]-2*K[t]
    return (K,D,J)

#计算相对强弱指标RSI
def RSI(data,N):
    import numpy as np
    z=np.zeros(len(data)-1) 
    z[data.iloc[1:,5].values-data.iloc[0:-1,5].values>=0]=1
    z[data.iloc[1:,5].values-data.iloc[0:-1,5].values<0]=-1
    z1=pd.rolling_sum(z==1,N)
    z2=pd.rolling_sum(z==-1,N)
    rsi=np.zeros((len(data)))
    for t in range(N-1,len(data)-1):
        rsi[t]=z1[t]/(z1[t]+z2[t])
    return rsi

def BIAS(data,N):
    import numpy as np
    bias=np.zeros((len(data)))
    man=pd.rolling_mean(data.iloc[:,5].values,N)
    for t in range(N-1,len(data)):
        bias[t]=(data.iloc[t,5]-man[t])/man[t]
    return bias

def OBV(data):
    import numpy as np
    obv=np.zeros((len(data)))
    for t in range(len(data)):
        if t==0:
            obv[t]=data['vol'].values[t]
        if t>0:
            if data['close'].values[t]>=data['close'].values[t-1]:
                obv[t]=obv[t-1]+data['vol'].values[t]
            if data['close'].values[t]<data['close'].values[t-1]:
                obv[t]=obv[t-1]-data['vol'].values[t]
    return obv

def cla(data):
    import numpy as np
    y=np.zeros(len(data)) 
    z=np.zeros(len(y)-1)
    z[data.iloc[1:,5].values-data.iloc[1:,2].values>0]=1
    z[data.iloc[1:,5].values-data.iloc[1:,2].values==0]=0
    z[data.iloc[1:,5].values-data.iloc[1:,2].values<0]=-1
    for i in range(len(z)):
        y[i]=z[i]  
    return y