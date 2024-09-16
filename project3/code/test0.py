# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:33:18 2024

@author: gaoya
"""

#加载必要的模块
import pandas as pd
# 读取文本数据

data = pd.read_csv('weibo_senti_100k.csv')
data = data.dropna()   #去掉数据集的空值
data.shape  #输出数据结构
data1=data.head()  # 输出文本数据集的前5行


# ## jieba分词 
import jieba
data['data_cut'] = data['review'].apply(lambda x: list(jieba.cut(x)))  #内嵌自定义函数来分词
data2= data.head()

# ##  去停用词

# 读取停用词
with open('stopword.txt','r',encoding = 'utf-8') as f:  #读取停用词
    stop = f.readlines()
# 对停用词处理
import re
stop = [re.sub(' |\n|\ufeff','',r) for r in stop]   #替换停用词表的空格等

# 去除停用词
#把分词之后的文本根据停用词表去掉停用词
data['data_after'] = [[i for i in s if i not in stop] for s in data['data_cut']]
data3=data.head()

# 构建词云
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# ## 词频统计
# 重组词组
num_words = [''.join(i) for i in data['data_after']] #把所有词组提取出来
num_words = ''.join(num_words)  #词组放在num_words上
num_words= re.sub(' ','',num_words)

# 计算全部词频
num = pd.Series(jieba.lcut(num_words)).value_counts()
# 用wordcloud画图
wc_pic = WordCloud(background_color='white',font_path=r'C:\Windows\Fonts\simhei.ttf').fit_words(num)
plt.figure(figsize=(10,10))  #图片大小定义
plt.imshow(wc_pic)#输出图片
plt.axis('off')#不显示坐标轴
plt.show()
 

