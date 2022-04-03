# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:24:16 2022
MONGO TO PANDAS
@author: pmcen
"""

import pymongo
import pandas as pd
from pymongo import MongoClient
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient()
#point the client at mongo URI
client = MongoClient('mongodb://192.168.56.30:27017')
#select database
db = client['crop_record_database']
#select the collection within the database
test = db.posts
#convert entire collection to Pandas dataframe
test = pd.DataFrame(list(test.find()))
#rename columns 
test.columns = ['id', 'state_name', 'district_name', 'crop_year', 'season', 'crop', 'area', 'production']
maize = test[test["crop"] == "Maize"]
rice = test[test["crop"] == "Rice"]
Tobacco = test[test["crop"] == "Tobacco"]
crop_names = test.crop.unique() # get all the possible crop names as an array

# CLEAN DATA
# check or NaN
test.production.isnull().values.any()
# returns false, no NaN present in dataframe 
#count the zero values in dataframe
counts_zero = (test == 0).sum()
print("count the zeros: \n", counts_zero) # no zero values in data frame 
#check data types 
print("data types ; \n", test.dtypes)
# re assign the data types 
"""
test.id.astype()
test.state_name.to_string()
test.district_name.to_string()
test.season.to_string()
test.crop.to_string()
"""
# "NA" values in production, remove this rows 
# lets rename the dataframe from test to df
df = test 
#4079 NAs found 
NAs = df[df.production == "NA"]
df = df[df.production != "NA"] # remove row with "NA" in production 
#check data types again
print("data types no na; \n", df.dtypes)
#now change column to numeric 
pd.to_numeric(df.production) # Still an object !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#check data types again
print("data types after change to production; \n", df.dtypes)
# WRITE FOR LOOP TO REPLACE NAs AS DECRIBED IN LOG 

""" can't do this without numeric data types 
# CHECK DISTRIBUTIONS 
# Boxplots 
sns.boxplot(y = 'production', x = 'crop', data = df1 )
# check each crop type for outliers 
for i in crop_names:
    print(i)    
"""