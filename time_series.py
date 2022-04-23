# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 17:04:33 2022

@author: pmcen
"""

# check cleaned data on mongoDB

import pymongo
import time
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
ax.bar_label(hbars, labels=[f'Records: {r}' for r in records_kept],
             padding=8,  fontsize=14)
ax.set_xlim(right=83)

plt.show()




