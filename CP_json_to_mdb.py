# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 13:32:47 2022

Get crop_records.json to a mondodb file

@author: pmcen
"""

import json
import pymongo

with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_records.JSON') as f:
  data = json.load(f)
recs = data["records"]
with open('crop_record_no_desc.json', 'w', encoding='utf-8') as f:
    json.dump(recs, f, ensure_ascii=False, indent=4)  # create json that only contains records, no info about file source/describtion etc 
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

# need to start running a mongoDB instance on VM before this step  
from pymongo import MongoClient   #create a MongoClient to the running mongod instance.
client = MongoClient(host = '192.168.56.30:27017')

db = client['crop_record_database']
collection = db['crop-record-collection']
#post docs too mongoDB, orig. doc is too large, post year by year 
#posts = db.posts 
#post_id = posts.insert_one(recs).inserted_id
