# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:29 2020

@author: Mason
"""

import requests
import pandas

# Years to be input into the API request
years = [2001,2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
yearCount = 0
API_Limit = 500000

# Dictionary to store DataFrames for each given year
dataframes = dict.fromkeys(years)

# API request for given year (1,000,000 records) into cleaned DataFrame
def getCrimeData(year, yearCount):
    request = requests.get(f'https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit={API_Limit}&year={year}').json()
    df = pandas.DataFrame.from_records(request)
    print(f'\n{year} Pre-Filter Count: {len(df)}')
    df = df.set_index('id')
    df = df.drop(['case_number', 'domestic', 'beat', 'district', 'ward', 'fbi_code', 'updated_on', 'x_coordinate', 'y_coordinate', 'community_area', 'arrest'], axis = 1)
    df = df.dropna()
    df = df[(df.longitude>='-87.6226')&(df.longitude<='-87.6260')&(df.latitude>='41.88843809')&(df.latitude<='41.90051916')]
    df['year'] = year
    dataframes[year] = df
    print(f'    Post-Filter Count: {len(df)}')     
    df.to_csv('.\output\\' + str(year) + 'CrimeData.csv') 
    # Start and append to "All" records csv
    if yearCount == 0:
        df.to_csv('.\output\All_CrimeData.csv') 
    else:
        df.to_csv('.\output\All_CrimeData.csv', mode='a', header=False) 

    
# For loop that iterates through given years; creatings csv file, DataFrame
for year in years:
    getCrimeData(year, yearCount)
    yearCount +=1
print(f'\nNumber of years processed: {yearCount}')
