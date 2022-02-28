# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 19:28:15 2022

@author: pmcen
"""

# nfl game stats data pull from profootball api

import requests
import pycurl
## WON'T GET API, NOT AUTHORISED TO PULL HISTORICAL DATA. ENQUIRY MADE WITH SITE HOST, AWAITING RESPONSE
api_call =  'https://profootballapi.com/schedule/'
api_req = requests.post(url=api_call, data='api_key = MGTPj4HvS9u3c0WnY7ObIl521ymtaKsC')

res = api_req.json() # get api request in json format



