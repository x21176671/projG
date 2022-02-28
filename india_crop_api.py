# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:47:36 2022

@author: pmcen
"""
import requests
import json
import csv

# India crops api 
api_key = "579b464db66ec23bdd0000010b46e55247d744b7680bb732c208ced6"
url = "https://api.data.gov.in/resource/35be999b-0208-4354-b557-f6ca9a5355de?api-key={}&format={}&offset=0&limit=246091"
#set offset to zero so no records skipped. set limit to full size of api to get all years records. will trip down later within the DataBase
url = url.format(api_key, 'json') #format my api key into url string and set format to pull 'json'
response = requests.get(url)
result = response.json()
crop_records = result["records"]
#write to csv 
with open('crop_records.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(crop_records[0].keys()) #turn the dict keys to header of the csv
    # write multiple rows
    rows = []
    for i in range(0,246091):
        rows.append(crop_records[i].values())
    writer.writerows(rows)













