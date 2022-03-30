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
crops2006 = []  
crops2005 = []  
crops2004 = []  
crops2003 = []  
crops2002 = []  
crops2001 = []  
crops2000 = []  
crops1999 = []  
crops1998 = []  
crops1997 = []  
crops1996 = []  
crops1995 = []  

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
with open('crop_record2006.json', 'w', encoding='utf-8') as f:
    json.dump(crops2006, f, ensure_ascii=False, indent=4)
with open('crop_record2005.json', 'w', encoding='utf-8') as f:
    json.dump(crops2005, f, ensure_ascii=False, indent=4)
with open('crop_record2004.json', 'w', encoding='utf-8') as f:
    json.dump(crops2004, f, ensure_ascii=False, indent=4)
with open('crop_record2003.json', 'w', encoding='utf-8') as f:
    json.dump(crops2003, f, ensure_ascii=False, indent=4)
with open('crop_record2002.json', 'w', encoding='utf-8') as f:
    json.dump(crops2002, f, ensure_ascii=False, indent=4)
with open('crop_record2001.json', 'w', encoding='utf-8') as f:
    json.dump(crops2001, f, ensure_ascii=False, indent=4)
with open('crop_record2000.json', 'w', encoding='utf-8') as f:
    json.dump(crops2000, f, ensure_ascii=False, indent=4)
with open('crop_record1999.json', 'w', encoding='utf-8') as f:
    json.dump(crops1999, f, ensure_ascii=False, indent=4)
with open('crop_record1998.json', 'w', encoding='utf-8') as f:
    json.dump(crops1998, f, ensure_ascii=False, indent=4)
with open('crop_record1997.json', 'w', encoding='utf-8') as f:
    json.dump(crops1997, f, ensure_ascii=False, indent=4)
with open('crop_record1996.json', 'w', encoding='utf-8') as f:
    json.dump(crops1996, f, ensure_ascii=False, indent=4)
with open('crop_record1995.json', 'w', encoding='utf-8') as f:
    json.dump(crops1995, f, ensure_ascii=False, indent=4)
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
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2006.JSON') as f:
  crop2006data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2005.JSON') as f:
  crop2005data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2004.JSON') as f:
  crop2004data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2003.JSON') as f:
  crop2003data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2002.JSON') as f:
  crop2002data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2001.JSON') as f:
  crop2001data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record2000.JSON') as f:
  crop2000data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record1999.JSON') as f:
  crop1999data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record1998.JSON') as f:
  crop1998data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record1997.JSON') as f:
  crop1997data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record1996.JSON') as f:
  crop1996data = json.load(f)
with open('C:/Users/pmcen/OneDrive/Documents/college/nci/semester1/database_and_analytics_programming/project/crop_record1995.JSON') as f:
  crop1995data = json.load(f)

# need to start running a mongoDB instance on VM before this step  
from pymongo import MongoClient   #create a MongoClient to the running mongod instance.
client = MongoClient('mongodb://192.168.56.30:27017')

db = client['crop_record_database']
collection = db['crop-record-collection']
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

import pprint
for post in posts.find():
    pprint.pprint(post)
#pprint.pprint(posts.find_one())





