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
crop_names = test.crop.unique() # get all the possible crop names as an array

# CLEAN DATA
# lets rename the dataframe from test to df
df = test 
df_na_full_sub = test # swap all na values with average for all other values of the same data type 
#4079 NAs found 
NAs = df[df.production == "NA"]
df = df[df.production != "NA"] # remove row with "NA" in production 

#now change column to numeric 
pd.to_numeric(df.production) # Still an object !!! can't parse "NA"
#test.astype({'production':'float64'})
#check data types again
print("data types after change to production; \n", test.dtypes)
# WRITE FOR LOOP TO REPLACE NAs AS DECRIBED IN LOG 
NAs = NAs.reset_index()
df = df.reset_index()        # reset indexes to get below loop operational                                
df_na_full_sub = df_na_full_sub.reset_index()
countNA = len(NAs[NAs.production=="NA"])    # amount of nas before cleaning 
NAs['production_cc'] = NAs['production'] # create new column for production to replace NAs with only previous years average

NAs = NAs.reset_index()
# FIND THE TROUBLE MAKERS (CROP/STATE/DISTRICT)
#use full avg, too many additional NAs. time period too short to worry about GW skewing the trend 
NA_states = []
NA_districts = []
NA_crops = []
for i in range(0, len(NAs)):
    if NAs.production[i] == "NA":
        NA_states.append(NAs.state_name[i]) # add state name for NA 
        NA_districts.append(NAs.district_name[i]) # add district name for NA 
        NA_crops.append(NAs.crop[i]) # add crops name for NA 

#remove TROUBLE MAKERS (CROP/STATE/DISTRICT)
df_no_bad_states = df_na_full_sub[~df_na_full_sub.state_name.isin(NA_states)] # remove all values from states that have any NAs 
# the above will remove more than just NAs but will yield consistency in TS. data is enormous anyway so needed to subset by something
# doing it this way kills 2 birds with one stone. ~23% of data remains 
df_na_full_sub = df_na_full_sub[df_na_full_sub.production!="NA"] #minimal data filtering, may have empty values in TS

# need to write df_no_bad_states to mongoDB but first ensure no NA's or averages carry over 
clean = db.clean
result = clean.insert_many(df_no_bad_states.to_dict('records'))
result.inserted_ids
    







 




















