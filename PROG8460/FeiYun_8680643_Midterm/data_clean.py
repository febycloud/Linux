#!/usr/bin/env python

#PROG8460 Midterm
#Fei Yun
#8680643

import pandas as pd
import numpy as np

#read overview sheet
df=pd.read_excel('Startups dataset.xlsx',sheet_name='Overview')
data=df[['ID','Name','Industry','Description','Year Founded','Employees','State','City','Metro Area']]
#drop duplicated records
data=data.drop_duplicates(['ID'])
print(data.count())

#fill description with NA
data['Description']=data['Description'].fillna('NA')
#find NA description belong to which industry
industry=data.loc[data['Description']=='NA','Industry']
print(industry)
#now we know the industry is Security,so find a decription of this industry
description=data.loc[data['Industry']=='Security','Description']
print(description)
#now we can replace with Description which is index 173 which is a good description of it
print(data.loc[data['ID']==173,'Description'])
#replace the data at xlsx where the Description is NA
data['Description']=data['Description'].replace(['NA'],'Specializes in information security, governance, and compliance.')

#fill metro area with NA
data['Metro Area']=data['Metro Area'].fillna('NA')
#find all NA metro's City
metro=data.loc[data['Metro Area']=='NA','City']
#the city list in NA metro
print(metro)
#find the city's Metro are in list NA,most of metro are different with city
citylist=data.loc[(data['City'].isin(metro))&(data['Metro Area']!='NA'),['City','Metro Area']].drop_duplicates(['City'])
print(citylist)
# replace data at xlsx file
# 1 metro in city list replace with its metro area
# 2 metro not in city list, it is small city so metro is the city itself
data.loc[(data['City']=='Orlando'),'Metro Area']='Orlando, FL'
data.loc[(data['City']=='Chicago'),'Metro Area']='Chicago'
data.loc[(data['City']=='Nashville'),'Metro Area']='Nashville'
data.loc[(data['City']=='Bellevue'),'Metro Area']='Seattle'
data.loc[(data['City']=='Chandler'),'Metro Area']='Phoenix'
data.loc[(data['City']=='Clarksville'),'Metro Area']='Clarksville'
data.loc[(data['City']=='Wayland'),'Metro Area']='Wayland'
data.loc[(data['City']=='Worley'),'Metro Area']='Worley'
data.loc[(data['City']=='Rockland'),'Metro Area']='Rockland'
data.loc[(data['City']=='Spanish Fork'),'Metro Area']='Spanish Fork'
#write overview sheet
writer=pd.ExcelWriter('cleaned_dataset.xlsx')
data.to_excel(writer,sheet_name='Overview',index=False)
#read financial sheet
data2=pd.read_excel('Startups dataset.xlsx',sheet_name='Financials')
data2.to_excel(writer,sheet_name='Financials',index=False)
#save sheet
writer.save()
#count the data record in new file
cleaned_df=pd.read_excel('cleaned_dataset.xlsx',sheet_name='Overview')
cleaned_data=cleaned_df[['ID','Name','Industry','Description','Year Founded','Employees','State','City','Metro Area']]

print(cleaned_data.count())