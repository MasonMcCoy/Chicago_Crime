# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:29 2020

@author: Mason
"""

import requests
import pandas

# Years to be input into the API request
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

# Dictionary to store DatFrames for each given year
dataframes = dict.fromkeys(years)

# API request for given year (1,000,000 records) into cleaned DataFrame
def getCrimeData(year):
    request = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=1000000&year=' + str(year)).json()
    df = pandas.DataFrame.from_records(request)
    df = df.set_index('id')
    df = df.drop(['case_number', 'domestic', 'beat', 'district', 'ward', 'fbi_code', 'year', 'updated_on', 'x_coordinate', 'y_coordinate', 'community_area', 'arrest'], axis = 1)
    df = df.dropna()
    df = df[df.longitude >= '-87.6226'] # -87.62418511
    df = df[df.longitude <= '-87.6260']
    df = df[df.latitude >= '41.88843809']
    df = df[df.latitude <= '41.90051916']          
    df.to_csv(r'C:\Users\Mason\Desktop\Crime Test\ ' + str(year) + 'CrimeData.csv')
    dataframes[year] = df

# For loop that iterates through given years; creatings csv file, DataFrame
for year in years:
    getCrimeData(year)