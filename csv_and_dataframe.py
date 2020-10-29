# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:29 2020

@author: Mason
"""
import requests
import pandas
import matplotlib.pyplot as plt
# import numpy as np

# Years to be input into the API request
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
yearCount = 0
API_Limit = 500000

# Dictionary to store DataFrames for each given year
dataframes = dict.fromkeys(years)

# API request for given year (1,000,000 records) into cleaned DataFrame
def getCrimeData(year, yearCount):
    request = requests.get(f'https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit={API_Limit}&year={year}').json()
    df = pandas.DataFrame.from_records(request)
    print(f'\n{year} Pre-Filter Count: {len(df)}')
    df = df.drop(['case_number', 'domestic', 'beat', 'district', 'ward', 'fbi_code', 'updated_on', 'x_coordinate', 'y_coordinate', 'community_area', 'arrest'], axis = 1)
    df = df.dropna()
    df = df[(df.longitude>='-87.6226')&(df.longitude<='-87.6260')&(df.latitude>='41.88843809')&(df.latitude<='41.90051916')]
    dataframes[year] = df
    print(f'    Post-Filter Count: {len(df)}')     

    # CC added Tom's bar charts (Oct28)
    top_10_list = df.groupby(["iucr","primary_type","description"]).count()
    top_10_df = pandas.DataFrame(top_10_list)
    top_10_df.rename(columns = {'id':'count'}, inplace = True) 
    top_10_df.reset_index(drop=False,inplace=True)
    top_10_df.sort_values(by=['count'], ascending = False, inplace = True)
    top_10_df = top_10_df.head(10)
    top_10_df.sort_values(by=["iucr"], ascending = True, inplace = True)
    offenses=top_10_df["primary_type"]+" / "+top_10_df["description"]
    plt.title("Top 10 Offenses for " + str(year))
    plt.xlabel("Criminal Offense")
    plt.ylabel("Criminal Offense Count")
    plt.bar(offenses, top_10_df["count"], color='b', align="center")
    plt.xticks(rotation=60,horizontalalignment='right')
    plt.figure(figsize=[10,4.8])
    plt.savefig(".\output\\" + str(year) + "Top10_Offenses.png")
    # End of TOm's stuff (Oct28)

    df.to_csv('.\output\\' + str(year) + 'CrimeData.csv', index = False) 
    # Start and append to "All" records csv
    if yearCount == 0:
        df.to_csv('.\output\All_CrimeData.csv', index = False) 
    else:
        df.to_csv('.\output\All_CrimeData.csv', mode='a', header=False, index = False) 

# For loop that iterates through given years; creatings csv file, DataFrame
for year in years:
    getCrimeData(year, yearCount)
    yearCount +=1
print(f'\nNumber of years processed: {yearCount}')
