# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:39:20 2022

@author: pmcen
"""
import requests 
from bs4 import BeautifulSoup
import pandas as pd
import lxml


URL = "https://www.worldometers.info/coronavirus/"
page = requests.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id = "all_team_stats")

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')
#soup

table1 = soup.find("table", id="team_stats")
table1