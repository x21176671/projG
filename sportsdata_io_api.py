# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:10:08 2022

@author: pmcen
"""


# nfl game stats data pull from sportsdata.io api

import requests
## WON'T GET API, NOT AUTHORISED TO PULL HISTORICAL DATA. ENQUIRY MADE WITH SITE HOST, AWAITING RESPONSE
api_call =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/{year}/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
api_req = requests.get(api_call)
result = api_req.json() # get api request in json format
"""
all_games = []
for n in range(2014, 2020): #don't include 21 as they changed the number of game weeks in reg. season to 18
    api_call = api_call.replace('{year}', str(n))
    for i in range(1,17):
        api_call = api_call.replace('{week}', str(i))
        api_req = requests.get(api_call)
        result = api_req.json() # get api request in json format
        all_games.append(result)

api_call = api_call.replace('{year}', str(2021)) # do 2021 season separate
for i in range (1, 18):
    api_call = api_call.replace('{week}', str(i))
    api_req = requests.get(api_call)
    result = api_req.json() # get api request in json format
    all_games.append(result)"""
"""
# 2020 season seems to work outside the loop ???????????????  
api_call20 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2020/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result20 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    api_call20 = api_call20.replace('{week}', str(n))
    api_req20  = requests.get(api_call20)
    result20.append(api_req20.json()) # get api request in json format
2020 is working """ 
"""
#2019 season
api_call19 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2019/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result19 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    api_call19 = api_call20.replace('{week}', str(n))
    api_req19  = requests.get(api_call19)
    result19.append(api_req19.json()) # get api request in json format
2019 is working"""
#2018 season
api_call18 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2018/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result18 = [] 
for n in range(1,18):
    api_call18 = api_call18.replace('{week}', str(n))
    api_req18  = requests.get(api_call18)
    result18.append(api_req18.json()) # get api request in json format

#2017 season
api_call17 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2017/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result17 = [] 
for n in range(1,18):
    api_call17 = api_call17.replace('{week}', str(n))
    api_req17  = requests.get(api_call17)
    result17.append(api_req17.json()) # get api request in json format

"""
#2016 season
api_call16 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2016/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result16 = [] 
for n in range(1,18):
    api_call16 = api_call20.replace('{week}', str(n))
    api_req16  = requests.get(api_call16)
    result16.append(api_req16.json()) # get api request in json format
2016 is working """
#2015 season
api_call15 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2015/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result15 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    api_call15 = api_call15.replace('{week}', str(n))
    api_req15  = requests.get(api_call15)
    result15.append(api_req15.json()) # get api request in json format
#2014 season
api_call14 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2014/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result14 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    api_call14 = api_call15.replace('{week}', str(n))
    api_req14  = requests.get(api_call14)
    result14.append(api_req14.json()) # get api request in json format
"""
#2021 season
api_call21 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2021/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
result21 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    api_call21 = api_call21.replace('{week}', str(n))
    api_req21 = requests.get(api_call21)
    result21.append(api_req21.json()) # get api request in json format
2021 season is working"""
#try load '21 again, could be a single use api pull issue     
#2021 season 2nd api pull test 
test_api_call21 =  'https://api.sportsdata.io/v3/nfl/scores/json/TeamGameStats/2021/{week}?key=6ae40a543f5142d2a6d48987bb188e9d'
test_result21 = []  # for some reason the 2020 season works in this loop but not above, will try each season this way 
for n in range(1,18):
    test_api_call21 = test_api_call21.replace('{week}', str(n))
    test_api_req21 = requests.get(test_api_call21)
    test_result21.append(test_api_req21.json()) # get api request in json format
#allowed pull 2021 data, not multiple pull issue 
    

