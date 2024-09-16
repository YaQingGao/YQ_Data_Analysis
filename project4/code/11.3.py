# -*- coding: utf-8 -*-
import os
file='F:\\新教材资料\\水色图像水质评价\\图片'
d=os.listdir(file)   #所有图片文件名
path=file+'\\'+d[0]  #第一个图片文件的完整路径
print(path)

from PIL import Image
import numpy as np
img = Image.open(path) #读取图片
img=img.resize((60,60)) #更改图片大小
im= img.split()        #分离RGBA通道
R=im[0]
G=im[1]
B=im[2]
img1=img.convert('L') #转化为灰图
img1=np.array(img1)   #将图像类型转换为整型
import matplotlib.pyplot as plt
plt.imshow(img1,cmap='gray') 
plt.show() #显示灰图
