# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:36:04 2022

all crop production code in one script to improve the automation of the analysis. 

@author: pmcen
"""

import requests
import json

# India crops api 
api_key = "579b464db66ec23bdd0000010b46e55247d744b7680bb732c208ced6"
url = "https://api.data.gov.in/resource/35be999b-0208-4354-b557-f6ca9a5355de?api-key={}&format={}&offset=0&limit=246091"
#set offset to zero so no records skipped. set limit to full size of api to get all years records. will trip down later within the DataBase
url = url.format(api_key, 'json') #format my api key into url string and set format to pull 'json'
response = requests.get(url)
result = response.json()
crop_records = result["records"]

# write full json import (not just records as above) to json file
with open('crop_records.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# reopen file to tidy up json to include only the dictionary of the records (initial json was 2 item dict 1 describtive, 1 containing all records as a nested dict)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_records.JSON') as f:
    data = json.load(f)
recs = data["records"]

with open('crop_record_no_desc.json', 'w', encoding='utf-8') as f:
    json.dump(recs, f, ensure_ascii=False, indent=4)  # create json that only contains records, no info about file source/describtion etc 

# Need to split Data by year to post to mongoDB as the file is too large to post all at once (>200,000 records)
crops2015 = []  #empty lists to store each years records 
crops2014 = []  
crops2013 = []  
crops2012 = []  
crops2011 = []  
crops2010 = []  
crops2009 = []  
crops2008 = []  
crops2007 = []  
for i in range(len(recs)): # fill each year with appropriate dicts 
    if recs[i]["crop_year"] == 2015:
        crops2015.append(recs[i])
    if recs[i]["crop_year"] == 2014:
        crops2014.append(recs[i])
    if recs[i]["crop_year"] == 2013:
        crops2013.append(recs[i])
    if recs[i]["crop_year"] == 2012:
        crops2012.append(recs[i])
    if recs[i]["crop_year"] == 2011:
        crops2011.append(recs[i])
    if recs[i]["crop_year"] == 2010:
        crops2010.append(recs[i])
    if recs[i]["crop_year"] == 2009:
        crops2009.append(recs[i])
    if recs[i]["crop_year"] == 2008:
        crops2008.append(recs[i])
    if recs[i]["crop_year"] == 2007:
        crops2007.append(recs[i])
with open('crop_record2015.json', 'w', encoding='utf-8') as f: #save individual jsons
    json.dump(crops2015, f, ensure_ascii=False, indent=4)
with open('crop_record2014.json', 'w', encoding='utf-8') as f:
    json.dump(crops2014, f, ensure_ascii=False, indent=4)
with open('crop_record2013.json', 'w', encoding='utf-8') as f:
    json.dump(crops2013, f, ensure_ascii=False, indent=4)
with open('crop_record2012.json', 'w', encoding='utf-8') as f:
    json.dump(crops2012, f, ensure_ascii=False, indent=4)
with open('crop_record2011.json', 'w', encoding='utf-8') as f:
    json.dump(crops2011, f, ensure_ascii=False, indent=4)
with open('crop_record2010.json', 'w', encoding='utf-8') as f:
    json.dump(crops2010, f, ensure_ascii=False, indent=4)
with open('crop_record2009.json', 'w', encoding='utf-8') as f:
    json.dump(crops2009, f, ensure_ascii=False, indent=4)
with open('crop_record2008.json', 'w', encoding='utf-8') as f:
    json.dump(crops2008, f, ensure_ascii=False, indent=4)
with open('crop_record2007.json', 'w', encoding='utf-8') as f:
    json.dump(crops2007, f, ensure_ascii=False, indent=4)
# read back in the jsons as dict
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2015.JSON') as f:
  crop2015data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2014.JSON') as f:
  crop2014data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2013.JSON') as f:
  crop2013data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2012.JSON') as f:
  crop2012data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2011.JSON') as f:
  crop2011data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2010.JSON') as f:
  crop2010data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2009.JSON') as f:
  crop2009data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2008.JSON') as f:
  crop2008data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2007.JSON') as f:
  crop2007data = json.load(f)

# need to start running a mongoDB instance on VM before this step  
from pymongo import MongoClient   #create a MongoClient to the running mongod instance.
client = MongoClient('mongodb://192.168.56.30:27017')

db = client['crop_record_database']
collection = db['crop_record_collection']
#post docs too mongoDB, orig. doc is too large, post year by year 
posts = db.posts 
result = posts.insert_many(crop2015data)
result.inserted_ids
result = posts.insert_many(crop2014data)
result.inserted_ids
result = posts.insert_many(crop2013data)
result.inserted_ids
result = posts.insert_many(crop2012data)
result.inserted_ids
result = posts.insert_many(crop2011data)
result.inserted_ids
result = posts.insert_many(crop2010data)
result.inserted_ids
result = posts.insert_many(crop2009data)
result.inserted_ids
result = posts.insert_many(crop2008data)
result.inserted_ids
result = posts.insert_many(crop2007data)
result.inserted_ids

# TIME TO LOAD DATA FROM MongoDB database
import pandas as pd
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
# check or NaN
test.production.isnull().values.any()    # returns false, no NULL present in dataframe 
#count the zero values in dataframe
counts_zero = (test.production == 0).sum()
print("count the zeros: \n", counts_zero) # no zero values in data frame 
# "NA" values in production, remove these rows 
# lets rename the dataframe from test to df
df = test 
NAs = df[df.production == "NA"]
df = df[df.production != "NA"] # remove row with "NA" in production 
#check data types 
print("data types no na; \n", df.dtypes)
#now change column to numeric 
pd.to_numeric(df.production) # Still an object !!! can't parse "NA"
countNA = len(NAs[NAs.production=="NA"])    # amount of nas before cleaning 
""" THIS FOR LOOP WAS INTENDED FOR REPLACING NAs WITH THE AVERAGE VALUE 
    OF SIMILAR CROPS IN THE SAME DISTRICT AND SEASON OVER OTHER YEARS.
    THIS DIDN'T PAN OUT, IT PROVED MORE EFFICIENT TO SIMPLY REMOVE ANY STATES
    CONTAINING NAs FROM THE DATA TO BE ANALYSED    
# WRITE FOR LOOP TO REPLACE NAs AS DECRIBED IN LOG 
df_na_full_sub = df_na_full_sub.reset_index()
df_na_past_sub = df_na_past_sub.reset_index()
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
                        if df.crop_year[n] <= year:  # find non na with same or less year as na found 
                            replacers_cc.append(float(df.production[n]))  # add production value to list to average over 
                            avg_cc = round(np.average(replacers_cc), 2)  # average over all similar values found 
                            print("Climate change: \n", i, "out of " , len(NAs), " NAs")
                            print("average: ", avg_cc)
                            print(n, " out of ", len(df), "df w/o NAs")
                            NAs.production_cc[i] = avg_cc # replace na with average 
"""
# FIND THE TROUBLE MAKERS (CROP/STATE/DISTRICT)
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
#remove TROUBLE MAKERS (CROP/STATE/DISTRICT)
df_no_bad_states = test[~test.state_name.isin(NA_states)] # remove all values from states that have any NAs 
# the above will remove more than just NAs but will yield consistency in TS. data is enormous anyway so needed to subset by something
# doing it this way kills 2 birds with one stone. ~23% of data remains 
df_na_full_sub = test[test.production!="NA"] #minimal data filtering, may have empty values in TS

# need to write df_no_bad_states to mongoDB but first ensure no NA's or averages carry over 
clean = db.clean
result = clean.insert_many(df_no_bad_states.to_dict('records'))
result.inserted_ids
    
##########################################################
#       ANALYSIS
##########################################################
import matplotlib.pyplot as plt

client = MongoClient()
#point the client at mongo URI
client = MongoClient('mongodb://192.168.56.30:27017')
#select database
db = client['crop_record_database']
#select the collection within the database
df = db.clean
#convert entire collection to Pandas dataframe
df = pd.DataFrame(list(df.find()))
NAs = df[df.area == "NA"] # empty df, the data cleaning was a success 

# write code to make df ts friendly (seasons to 1-4 etc)

# count the amount of data by state and by crop 
from collections import Counter
states = list(df.state_name)
print("states: ")
Counter(states) 
crops = list(df.crop)
print("crops: ")
Counter(df.crop)

# CROP YIELD BY YEAR 
df2015 = df[df.crop_year == 2015]
df2014 = df[df.crop_year == 2014]
df2013 = df[df.crop_year == 2013]
df2012 = df[df.crop_year == 2012]
df2011 = df[df.crop_year == 2011]
df2010 = df[df.crop_year == 2010]
df2009 = df[df.crop_year == 2009]
df2008 = df[df.crop_year == 2008]
df2007 = df[df.crop_year == 2007]
crop_yield = []
years = [2007,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
spud_years = [2007,2008, 2009, 2010, 2011, 2012, 2013, 2014]
spuds = df[df.crop=="Potato"]
spud_yield =[]
for i in range(0, len(df[df.crop=="Potato"].crop_year.unique())):
    print("year: ", df[df.crop=="Potato"].crop_year.unique()[i])
    total_prod = sum(spuds[spuds.crop_year==df[df.crop=="Potato"].crop_year.unique()[i]].production)
    print(total_prod)
    total_area = sum(spuds[spuds.crop_year==df[df.crop=="Potato"].crop_year.unique()[i]].area)
    print(total_area)
    spud_yield.append(total_prod/total_area)
plt.xlabel("year")
plt.ylabel("yield")
plt.plot(spud_years, spud_yield)
plt.title("spuds")
plt.show()

#get this for all (more anyway ) crops 
crop_names = list(df.crop.unique()) # get all the possible crop names as an array
counter = 0
df = df.reset_index()
crop_anlys_names = []
for n in crop_names:            # get the names of all the crops with enough data to do effective time (yield or otherwise) analysis on 
    print(n)                                    
    c_df = df[df.crop==n]
    years =  list(c_df.crop_year.unique()) # get years for given crop 
    if len(years) >=8:
        crop_anlys_names.append(n)
print("good for analysis: ", crop_anlys_names)
df_time = df[df['crop'].isin(crop_anlys_names)] # subset dataframe to only include crops with data across many years 
# subset again by most records per year 
crop_names_time = list(df_time.crop.unique()) # get all the possible crop names for time analysis as an array
exc_crop = [] # exclude any crops with low amount of data in any given year
for n in crop_names_time:            # get the names of all the crops with enough data to do effective time (yield or otherwise) analysis on 
    print(n)                                    
    c_df = df_time[df_time.crop==n]
    years =  list(c_df.crop_year.unique()) # get years for given crop 
    recs_per_yr = []
    for i in years: # get the amount of data for each year for the given crop
        rec_per_yr = int(len(c_df[c_df.crop_year == i]))
        recs_per_yr.append(int(len(c_df[c_df.crop_year == i])))
        if rec_per_yr < 50  :
            exc_crop.append(n)
            print(n, "has low records (", rec_per_yr, ") for ", i)
    print(recs_per_yr)
exc_crop = list(set(exc_crop))  # remove duplicate values of crop names with low records in any year
print("bad for analysis: ", exc_crop)
df_time = df_time[~df_time['crop'].isin(exc_crop)] # subset dataframe to only include crops with data across many years 
crop_anlys_names = list(df_time.crop.unique()) # redefine the names of crops to be used for time analysis 

# YIELD ANALYSIS
exclude_yield = []
# loop for yield analysis
c_yield_2014 = []  # list for the crop yields from 2014 ( for sorting legend nicely)
for i in crop_anlys_names: # loop to find the 2014 yield for each crop being analysed below 
    c_df = df_time[df_time.crop == i]
    c_yield_2014.append(sum(c_df[c_df.crop_year==2014].production)/sum(c_df[c_df.crop_year==2014].area))
yield_dict2014 = dict(zip(crop_anlys_names, c_yield_2014)) # dictionary of crops being analysed and their yield in 2014 (end of yield analysis)
import operator
yield_dict2014 = dict( sorted(yield_dict2014.items(), key=operator.itemgetter(1),reverse=True)) #sort the dictionary by value
yield_dict2014_upper = yield_dict2014.copy()  # copy the dictionary to subset it for the plots of only the crops in the upper level plot for the report
low_yield_crops = ["Turmeric", "Black pepper", "Cotton(lint)", "Dry chillies", "Peas & beans (Pulses)",
                   "Gram", "Arhar/Tur", "Tobacco", "Masoor",
                   "Linseed", "Sesamum", "Moong(Green Gram)", "Castor seed"]  
for key in low_yield_crops:  # remove low yield crops 
    del yield_dict2014_upper[key] 
for n in yield_dict2014_upper.keys():
    c_yield =[]
    c_df = df_time[df_time.crop == n]
    years =  list(c_df.crop_year.unique()) # get years for given crop 
    try:
        for i in years:
            total_prod = sum(c_df[c_df.crop_year==i].production)
            total_area = sum(c_df[c_df.crop_year==i].area)
            c_yield.append(total_prod/total_area)
        plt.xlabel("year")
        plt.ylabel("yield (Tonnes/Hectare)")
        print(n, "\n", years, "\n yield: \n", c_yield)
        plt.plot(years, c_yield,'-o', label = n)
        plt.legend(loc = 10, ncol=1, bbox_to_anchor=(1.25, 0.5))
    except ZeroDivisionError: # catch mistakes in loop and poor input data 
        print(n, "has no area this year ", print(i))
        exclude_yield.append(i)
plt.title("Yield by crop (high) yield)" )
plt.show()

# YIELD ANALYSIS low yield crops 
exclude_yield = []
yield_dict2014_lower = yield_dict2014.copy() # copy the dictionary to subset it for the plots of only the crops in the lower level plot for the report
high_yield_crops = ["Sugarcane", "Banana", "Jute", "Tapioca", "Potato",
                   "Mesta", "Sweet potato", "Onion"]  
for key in high_yield_crops:  # remove low yield crops 
    del yield_dict2014_lower[key] 
# loop for yield analysis
for n in yield_dict2014_lower.keys():
    c_yield =[]
    c_df = df_time[df_time.crop == n]
    years =  list(c_df.crop_year.unique()) # get years for given crop 
    try:
        for i in years:
            total_prod = sum(c_df[c_df.crop_year==i].production)
            total_area = sum(c_df[c_df.crop_year==i].area)
            c_yield.append(total_prod/total_area)
        plt.xlabel("year")
        plt.ylabel("yield (Tonnes/Hectare)")
        print(n, "\n", years, "\n yield: \n", c_yield)
        plt.plot(years, c_yield, '-o', label = n)
        plt.legend(loc = 10, ncol=1, bbox_to_anchor=(1.25, 0.5))
    except ZeroDivisionError: # catch mistakes in loop and poor input data 
        print(n, "has no area this year ", print(i))
        exclude_yield.append(i)
plt.title("Yield by crop (low yield)")
plt.show()


# CROP DIVERSIFICATION 
years = [2007,2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]
crop_counts = []
records_kept = []
for y in years: 
    y_df = df[df.crop_year == y]
    crop_counts.append(len(y_df.crop.unique()))
    records_kept.append(len(y_df))
    print("year: ", y)
    print("unique crops: ", crop_counts)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
y_pos = np.arange(len(years))
hbars = ax.barh(y_pos, crop_counts, align='center')
ax.set_yticks(y_pos, labels=years)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('number of unique crops')
ax.set_title('Crop Diversification')

# Label with given captions, custom padding and annotate options
ax.bar_label(hbars, labels=[r for r in records_kept],
             padding=8,  fontsize=14)
ax.set_xlim(right=75)

plt.show()
 














 


