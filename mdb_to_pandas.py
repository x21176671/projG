# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 20:24:16 2022
MONGO TO PANDAS

COMPUTATIONALLY INTENSIVE SCRIPT ~ 2 HOURS TO RUN FOR LOOP 
@author: pmcen
"""

import pandas as pd
from pymongo import MongoClient
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
#test.production.isnull().values.any()
# returns false, no NaN present in dataframe 
#count the zero values in dataframe
counts_zero = (test.production == 0).sum()
print("count the zeros: \n", counts_zero) # no zero values in data frame 
#check data types 
print("data types ; \n", test.dtypes)
# "NA" values in production, remove these rows 
# lets rename the dataframe from test to df
df = test 
df_na_full_sub = test # swap all na values with average for all other values of the same data type 
df_na_past_sub = test
#4079 NAs found 
NAs = df[df.production == "NA"]
df = df[df.production != "NA"] # remove row with "NA" in production 
#check data types again
print("data types no na; \n", df.dtypes)
#now change column to numeric 
pd.to_numeric(df.production) # Still an object !!! can't parse "NA"
#test.astype({'production':'float64'})
#check data types again
print("data types after change to production; \n", test.dtypes)
# WRITE FOR LOOP TO REPLACE NAs AS DECRIBED IN LOG 
NAs = NAs.reset_index()
df = df.reset_index()        # reset indexes to get below loop operational                                
df_na_full_sub = df_na_full_sub.reset_index()
df_na_past_sub = df_na_past_sub.reset_index()
countNA = len(NAs[NAs.production=="NA"])    # amount of nas before cleaning 
NAs['production_cc'] = NAs['production'] # create new column for production to replace NAs with only previous years average
for i in range(0, len(NAs)): 
    state_name = str(NAs.state_name[i])  # state of na found
    district = str(NAs.district_name[i])  # district of na found
    season = str(NAs.season[i])   # season of na found
    crop = str(NAs.crop[i])  # crop of na found
    year = float(NAs.crop_year[i])  # year of na found
    replacers = []  #list to append values to average over to replace nas with 
    replacers_cc = []  #list to append values to average over to replace nas with only from past years (CC=> CLIMATE CHANGE )
    for n in range(0, len(df)): 
        if df.state_name[n] == state_name:  # find non na with same state as na found 
            if df.district_name[n] == district: # find non na with same district as na found 
                if df.season[n] == season: # find non na with same season as na found 
                    if df.crop[n] == crop:  # find non na with same crop as na found 
                        replacers.append(float(df.production[n]))  # add production value to list to average over 
                        avg = round(np.average(replacers), 2)  # average over all similar values found 
                        print(i, "out of " , len(NAs), " NAs")
                        print("average: ", avg)
                        print(n, " out of ", len(df), "df w/o NAs")
                        NAs.production[i] = avg # replace na with average 

print("NAs before cleaning", countNA)
print("NAs after cleaning full avg", len(NAs[NAs.production=="NA"]))
print("NAs after cleaning previous years avg", len(NAs[NAs.production_cc=="NA"]))
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
from collections import Counter
print("bad states: ")
Counter(NA_states) # count the NAs for each bad state 
print("bad districts: ")
Counter(NA_districts) # count the NAs for each bad district
print("bad crops: ")
Counter(NA_crops) # count the NAs for each bad crop 
# write NAs to csv and filter to find the best troublemakers to remove 
NAs.to_csv('NAs_cleaning.csv')

#removing the states with nas is the way to go, see data_cleaning1.py directly after running this script











 