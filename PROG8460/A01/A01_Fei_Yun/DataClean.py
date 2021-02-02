#!/usr/bin/python

import pandas as pd
import numpy as np

#read data from csv
df=pd.read_csv('Assignment1 Data Sample.csv')
#print(df.count())
#print(df.head())

#delete irrelevant colum
relevant_data=df[['Object Number','Object ID','Department','Object Name','Title','Object Begin Date','Object End Date','Medium','Link Resource']]
#print(relevant_data.head())
print(relevant_data.count())

#delete invaild row and duplicated row
data_vaild=relevant_data.dropna()
data_vaild=data_vaild.drop_duplicates(['Object ID'])
#data_vaild.to_csv('Assignment1_cleaned.csv',encoding='utf-8')

#How many data records are in your final dataset?
print(data_vaild.count())

#How many data records did you manually remove during the cleansing process?
print(204-185)

#How many countries of origin are contained in your final dataset? List them.
result=pd.merge(df,data_vaild,on=['Object ID'])
list_country=result['Country'].tolist()
list_country=set(list_country)
print(list_country)
print(len(list_country))