# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
#tushare API 初始化
ts.set_token('64532b1c03637bc0c3ac92931a5d1b53cfaf75de87c22dfdc70ca6a0')
pro = ts.pro_api()

#股票基本信息获取，并保持为Excel文件
stkcode = pro.stock_basic(exchange='', list_status='L', 
                          fields='ts_code,symbol,name,area,industry')
stkcode.to_excel('stkcode.xlsx')

#从利润表中获取营业收入、营业利润、利润总额、净利润指标数据
income= pro.income_vip(period='20161231',
        fields='ts_code,revenue,operate_profit,total_profit,n_income_attr_p')
income=income.drop_duplicates(subset=['ts_code'])

#从资产负债表中获取资产总计、固定资产指标数据
balance = pro.balancesheet_vip(period='20161231',
                               fields='ts_code,total_assets,fix_assets')
balance=balance.drop_duplicates(subset=['ts_code'])

#从财务指标表中获取净资产收益率、每股净资产、每股资本公积、每股收益指标数据
indicator=pro.fina_indicator_vip(period='20161231',
                                 fields='ts_code,roe,bps,capital_rese_ps,eps')
indicator=indicator.drop_duplicates(subset=['ts_code'])

#数据集成，以代码为键，内连接，并把集成后的数据导出Excel
tempdata=pd.merge(income,balance,how='inner',on='ts_code')
Data=pd.merge(tempdata,indicator,how='inner',on='ts_code')
Data.to_excel('Data.xlsx')

##另外，本章中的其他数据获取例子，也在本程序中
#获取上汽集团2017年的交易数据，并导出Excel
dta = pro.daily(ts_code='600104.SH', 
                start_date='20170101', end_date='20171231')
dta=dta.sort_values('trade_date')
dta.to_excel('dta.xlsx')

#获取沪深300指数2017年的交易数据，并导出Excel
hs300 = pro.index_daily(ts_code='399300.SZ', start_date='20170101', end_date='20171231')
hs300=hs300.sort_values('trade_date')
hs300.to_excel('hs300.xlsx')
