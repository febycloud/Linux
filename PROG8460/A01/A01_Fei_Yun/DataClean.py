
import pandas as pd
import numpy as np

#read data from csv
df=pd.read_csv('DataSample_step1.csv')
print("the sample data has" + str(df['Object ID'].count()))
#print(df.head())

#delete irrelevant colum
relevant_data=df[['Object Number','Object ID','Department','Object Name','Title','Culture','Period','Dynasty','Reign','Portfolio','Artist Role','Artist Prefix','Artist Display Name','Artist Suffix','Artist Nationality','Object Begin Date','Object End Date','Medium','Dimensions','Credit Line','Geography Type','City','State','Country','Region','Subregion','Locale','Locus','Excavation','River','Classification','Rights and Reproduction','Link Resource','Metadata Date','Repository','Tags']]
#print(relevant_data.head())
print("the relevant data has"+ str(relevant_data['Object ID'].count()))

#delete invaild row and duplicated row
data_vaild=relevant_data.dropna(axis=0,subset=['Object Number','Object ID','Department','Object Name','Object Begin Date','Object End Date','Medium','Link Resource'])
print("the requied data has"+ str(data_vaild['Object ID'].count()))
data_vaild=data_vaild.drop_duplicates(['Object ID'])
print("without duplicate has"+ str(data_vaild['Object ID'].count()))
data_vaild.to_csv('Assignment1_cleaned.csv',encoding='utf-8',index=False)

#How many data records are in your final dataset?
print("the final has" + str(data_vaild['Object ID'].count()))

#How many data records did you manually remove during the cleansing process?
print(204-195)

#How many countries of origin are contained in your final dataset? List them.

list_country=data_vaild['Country'].tolist()
list_country=set(list_country)
print(list_country)
print(len(list_country))