#!/usr/bin/env python

import pandas as pd
import numpy as np

#read data from csv
df=pd.read_csv('sample.csv')
data=df[['CustomerID','MonthlyCharges','TotalCharges','PaymentMethod','Churn']]
data=data.drop_duplicates(['CustomerID'])

print(data.count())

data['MonthlyCharges']=data['MonthlyCharges'].fillna('N/A')
data['MonthlyCharges']=data['MonthlyCharges'].replace(['Nan'],'N/A')

data['TotalCharges']=data['TotalCharges'].replace(['na','NA'],'N/A')
data['TotalCharges']=data['TotalCharges'].fillna('N/A')

data['PaymentMethod']=data['PaymentMethod'].fillna('--')
#data.to_csv('test_clean.csv')