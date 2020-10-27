# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:03:27 2020

@author: coffm
"""

#2001+ data w/example of 5000 limit
import requests
import pandas as pd
cityAPI = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=5000&$$app_token=yCkPkXAsAml5WGe3oM8SdnvpX&$limit=5000').json()
results_df = pd.DataFrame.from_records(cityAPI)
results_df.to_csv('CrimeData.csv')
print(results_df)

#2001+ data w/example of 5000 limit with block='008xx N MICHIGAN AVE"
import requests
import pandas as pd
cityAPI = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=5000&$$app_token=yCkPkXAsAml5WGe3oM8SdnvpX&block=008XX%20N%20MICHIGAN%20AVE').json()
results_df = pd.DataFrame.from_records(cityAPI)
results_df.to_csv('CrimeData.csv')
print(results_df)