# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 20:03:06 2022

@author: pmcen
"""
import requests
import json
import csv
import pandas as pd 
import sqlite3 

# crop records json to sql/mongoDB database

with open('crop_records.json', 'r') as f:
    data = json.loads(f)
"""
df = pd.DataFrame(crop_records) #turn crop records into a pandas dataframe 
#get dataframe into sql format (RELATIONAL DATABASE)
conn = sqlite3.connect('crop_records.db') #code from https://www.youtube.com/watch?v=lI3WiAmDvTw
c = conn.cursor()
df.to_sql("crop_records", conn) # dump df, created from json file, into sql db
"""























