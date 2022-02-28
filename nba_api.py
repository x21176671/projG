# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 12:22:36 2022

@author: pmcen
"""

#nba game logs 
#sportsdata costs a lot to get historical data, NBA  season is much longer so can use that to get 
#more data points to meet project requirements 
import requests
import json
import time 
import pandas 

#get all games for the 2017 season copied from api-nba site using their on site python guide
url = "https://api-nba-v1.p.rapidapi.com/games/seasonYear/2017"
headers = {
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
    'x-rapidapi-key': "6b32e387c3msh9c51963fe32d0e5p13f3afjsna2783cf62e8a"
    }
response = requests.request("GET", url, headers=headers)
result = response.json()
""" # save to json file
season2017 = response.json()
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(season2017, f, ensure_ascii=False, indent=4)
"""
#get the game id's for each game in the 2017 season
# TURN THESE LOOPS INTO A FUNCTION########################################################
################################################################################
test_gameIds2017 = [] 
for i in range(0,1466):  #there were 82 games per team, 30 teams so 1230 games total played in regular season
    print("loop iteration:", i) # json file seems to have more than 1230 entries, maxes out at 1466 interations
    print(result['api']['games'][i]['gameId']) 
    test_gameIds2017.append(result['api']['games'][i]['gameId'])
#get game stats using above list of game ids
test_game_stats_2017 = []
for i in test_gameIds2017:
    url = "https://api-nba-v1.p.rapidapi.com/statistics/games/gameId/{gameid}"
    url = url.replace('{gameid}', str(i))
    print(url) #let's check make sure it's loading the right url each time 
    headers = {
        'x-rapidapi-host': "api-nba-v1.p.rapidapi.com",
        'x-rapidapi-key': "6b32e387c3msh9c51963fe32d0e5p13f3afjsna2783cf62e8a"
        }
    response = requests.request("GET", url, headers=headers)
    time.sleep(6) # sleep loop for 6 seconds to keep api calls/minute low (we get 10 per minute 100 per day)    
    test_game_stats_2017.append(response.json())
"""
#write game_stats_2017 to a json file
season2017 = response.json()
with open('gamesdata2017.json', 'w', encoding='utf-8') as f:
    json.dump(game_stats_2017, f, ensure_ascii=False, indent=4)
"""


##############################################################################
#TOO UNRELATED TO OTHER SETS BY ANGELO AND LINA, REPORT WRITE UP COULD SUFFER#
# KEEP CODE FOR NOW AS THIS API MAY BE A GOOD FUTURE PROJECT ON THE COURSE ###
##############################################################################
