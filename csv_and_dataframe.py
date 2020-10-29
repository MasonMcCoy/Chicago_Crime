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

theft_values = []
theft_norms = []
decpra_values = []
decpra_norms = []
tres_values = []
tres_norms = []
batt_values = []
batt_norms = []
dam_values = []
dam_norms = []
assault_values = []
assault_norms = []
prost_values = []
prost_norms = []
narc_values = []
narc_norms = []
robb_values = []
robb_norms = []
ppv_values = []
ppv_norms = []
burg_values = []
burg_norms = []
llv_values = []
llv_norms = []
iwpo_values = []
iwpo_norms = []
homi_values = []
homi_norms = []
sa_values = []
sa_norms = []
mvtheft_values = []
mvtheft_norms = []
other_values = []
other_norms = []

# API request for given year (1,000,000 records) into cleaned DataFrame
def getCrimeData(year):
    request = requests.get('https://data.cityofchicago.org/resource/ijzp-q8t2.json?$limit=100000&year=' + str(year)).json()
    df = pandas.DataFrame.from_records(request)
    df = df.set_index('id')
    df = df.drop(['case_number', 'domestic', 'beat', 'district', 'ward', 'fbi_code', 'year', 'updated_on', 'x_coordinate', 'y_coordinate', 'community_area', 'arrest'], axis = 1)
    df = df.dropna()
    df = df[df.longitude >= '-87.6226'] 
    df = df[df.longitude <= '-87.6260']
    df = df[df.latitude >= '41.88843809']
    df = df[df.latitude <= '41.90051916']          
    df.to_csv(r'C:\Users\Mason\Desktop\Crime Test\ ' + str(year) + 'CrimeData.csv') #Use local file path
    dataframes[year] = df

# For loop that iterates through given years; creatings csv file, DataFrame
for year in years:
    getCrimeData(year)
    
for dataframe in dataframes:
    val = dataframes[dataframe]['primary_type'].value_counts()
    norm = dataframes[dataframe]['primary_type'].value_counts(normalize = True)
    norm = round((norm * 100), 2)
    
    try:
        theft_values.append(val['THEFT'])
        theft_norms.append(norm['THEFT'])
    except Exception:
        theft_values.append(0)
        theft_norms.append(0)
    try:
        decpra_values.append(val['DECEPTIVE PRACTICE'])
        decpra_norms.append(norm['DECEPTIVE PRACTICE'])
    except Exception:
        decpra_values.append(0)
        decpra_norms.append(0)
    try:
        tres_values.append(val['CRIMINAL TRESPASS'])
        tres_norms.append(norm['CRIMINAL TRESPASS'])
    except Exception:
        tres_values.append(0)
        tres_norms.append(0)
    try:
        batt_values.append(val['BATTERY'])
        batt_norms.append(norm['BATTERY'])
    except Exception:
        batt_values.append(0)
        batt_norms.append(0)
    try:
        dam_values.append(val['CRIMINAL DAMAGE'])
        dam_norms.append(norm['CRIMINAL DAMAGE'])
    except Exception:
        dam_values.append(0)
        dam_norms.append(0)
    try:
        assault_values.append(val['ASSAULT'])
        assault_norms.append(norm['ASSAULT'])
    except Exception:
        assault_values.append(0)
        assault_norms.append(0)
    try:
        prost_values.append(val['PROSTITUTION'])
        prost_norms.append(norm['PROSTITUTION'])
    except Exception:
        prost_values.append(0)
        prost_norms.append(0)
    try:
        narc_values.append(val['NARCOTICS'])
        narc_norms.append(norm['NARCOTICS'])
    except Exception:
        narc_values.append(0)
        narc_norms.append(0)
    try:
        robb_values.append(val['ROBBERY'])
        robb_norms.append(norm['ROBBERY'])
    except Exception:
        robb_values.append(0)
        robb_norms.append(0)
    try:
        ppv_values.append(val['PUBLIC PEACE VIOLATION'])
        ppv_norms.append(norm['PUBLIC PEACE VIOLATION'])
    except Exception:
        ppv_values.append(0)
        ppv_norms.append(0)
    try:
        burg_values.append(val['BURGLARY'])
        burg_norms.append(norm['BURGLARY'])
    except Exception:
        burg_values.append(0)
        burg_norms.append(0)
    try:
        llv_values.append(val['LIQUOR LAW VIOLATION'])
        llv_norms.append(norm['LIQUOR LAW VIOLATION'])
    except Exception:
        llv_values.append(0)
        llv_norms.append(0)
    try:
        iwpo_values.append(val['INTERFERENCE WITH PUBLIC OFFICER'])
        iwpo_norms.append(norm['INTERFERENCE WITH PUBLIC OFFICER'])
    except Exception:
        iwpo_values.append(0)
        iwpo_norms.append(0)
    try:
        homi_values.append(val['HOMICIDE'])
        homi_norms.append(norm['HOMICIDE'])
    except Exception:
        homi_values.append(0)
        homi_norms.append(0)
    try:
        sa_values.append(val['CRIMINAL SEXUAL ASSAULT'])
        sa_norms.append(norm['CRIMINAL SEXUAL ASSAULT'])
    except Exception:
        sa_values.append(0)
        sa_norms.append(0)
    try:
        mvtheft_values.append(val['MOTOR VEHICLE THEFT'])
        mvtheft_norms.append(norm['MOTOR VEHICLE THEFT'])
    except Exception:
        mvtheft_values.append(0)
        mvtheft_norms.append(0)
    try:
        other_values.append(val['OTHER OFFENSE'])
        other_norms.append(norm['OTHER OFFENSE'])
    except Exception:
        other_values.append(0)
        other_norms.append(0)

crimes = 'THEFT', 'DECEPTIVE PRACTICE', 'CRIMINAL TRESPASS', 'BATTERY', 'CRIMINAL DAMAGE', 'ASSAULT', 'PROSTITUION', 'NARCOTICS', 'ROBBERY', 'PUBLIC PEACE VIOLATION', 'BURGLARY', 'LIQUOR LAW VIOLATION', 'INTERFERENCE WITH PUBLIC OFFICER', 'HOMICIDE', 'CRIMINAL SEXUAL ASSAULT', 'MOTOR VEHICLE THEFT', 'OTHER OFFENSE'        
data = (theft_values, decpra_values, tres_values, batt_values, dam_values, assault_values, prost_values, narc_values, robb_values, ppv_values, burg_values, llv_values, iwpo_values, homi_values, sa_values, mvtheft_values, other_values)

valuesDF = pandas.DataFrame(data, columns = years)
valuesDF['Crime'] = crimes
valuesDF = valuesDF.set_index('Crime'
                              )
#normsDF = pandas.DataFrame(theft_norms, decpra_norms, tres_norms, batt_norms, dam_norms) #, assault_norms, prost_norms, narc_norms, robb_norms, ppv_norms, burg_norms, llv_norms, iwpo_norms, homi_norms, sa_norms, mvtheft_norms, other_norms)

print(valuesDF)
#print(normsDF)