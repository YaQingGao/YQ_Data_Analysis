# -*- coding: utf-8 -*-
import datetime
def find_I(h1,m1,h2,m2,D2,B):
   I1=B.iloc[:,4].values>=datetime.time(h1,m1)
   I2=B.iloc[:,4].values<=datetime.time(h2,m2)
   I3=D2<=5
   I=I1&I2&I3
   return I

