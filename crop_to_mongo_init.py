# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:31:36 2022

Create python script to connect to mongoDB on VM and set up a database
of the cropproduction.JSON file 

@author: pmcen
"""
import json
import pymongo
from pymongo import MongoClient

client = MongoClient(host = '192.168.56.30:27017')
db = client['crop_database']
collection = client['crop_collection']

































