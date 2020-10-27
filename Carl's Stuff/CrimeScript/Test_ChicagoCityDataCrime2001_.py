# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:03:27 2020

@author: coffm
"""
import requests
import pandas as pd
cityAPI = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2').json()
results_df = pd.DataFrame.from_records(cityAPI)
results_df.to_csv('..\CrimeData.csv')
print(results_df)
