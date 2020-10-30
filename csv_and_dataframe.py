# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:29 2020

@author: Mason
"""
import requests
import pandas
import matplotlib.pyplot as plt
# import numpy as np
import scipy.stats as st

# Years to be input into the API request
years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
yearCount = 0
API_Limit = 50000

# Dictionary to store DataFrames for each given year
dataframes = dict.fromkeys(years)

# Lists to store value_counts data
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
arson_values = []
arson_norms = []
so_values = []
so_norms = []
intim_values = []
intim_norms = []
wv_values = []
wv_norms = []
oic_values = []
oic_norms = []
pi_values = []
pi_norms = []
stalk_values = []
stalk_norms = []
kidn_values = []
kidn_norms= []
cclv_values = []
cclv_norms = []
obs_values = []
obs_norms = []
csa_values = []
csa_norms= []
nocrim_values = []
nocrim_norms = []
nocrim_values = []

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

# Isolates value_counts data(count and normalized) into respepctive lists    
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
    try:
        arson_values.append(val['ARSON'])
        arson_norms.append(norm['ARSON'])
    except Exception:
        arson_values.append(0)
        arson_norms.append(0)       
    try:
        so_values.append(val['SEX OFFENSE'])
        so_norms.append(norm['SEX OFFENSE'])
    except Exception:
        so_values.append(0)
        so_norms.append(0)
    try:
        intim_values.append(val['INTIMIDATION'])
        intim_norms.append(norm['INTIMIDATION'])
    except Exception:
        intim_values.append(0)
        intim_norms.append(0)
    try:
        wv_values.append(val['WEAPONS VIOLATION'])
        wv_norms.append(norm['WEAPONS VIOLATION'])
    except Exception:
        wv_values.append(0)
        wv_norms.append(0)
    try:
        oic_values.append(val['OFFENSE INVOLVING CHILDREN'])
        oic_norms.append(norm['OFFENSE INVOLVING CHILDREN'])
    except Exception:
        oic_values.append(0)
        oic_norms.append(0)
    try:
        pi_values.append(val['PUBLIC INDECENY'])
        pi_norms.append(norm['PUBLIC INDECENY'])
    except Exception:
        pi_values.append(0)
        pi_norms.append(0)
    try:
        stalk_values.append(val['STALKING'])
        stalk_norms.append(norm['STALKING'])
    except Exception:
        stalk_values.append(0)
        stalk_norms.append(0)    
    try:
        kidn_values.append(val['KIDNAPPING'])
        kidn_norms.append(norm['KIDNAPPING'])
    except Exception:
        kidn_values.append(0)
        kidn_norms.append(0)  
    try:
        cclv_values.append(val['CONCEALED CARRY LICENSE VIOLATION'])
        cclv_norms.append(norm['CONCEALED CARRY LICENSE VIOLATION'])
    except Exception:
        cclv_values.append(0)
        cclv_norms.append(0)  
    try:
        obs_values.append(val['OBSCENITY'])
        obs_norms.append(norm['OBSCENITY'])
    except Exception:
        obs_values.append(0)
        obs_norms.append(0)  
    try:
        csa_values.append(val['CRIM SEXUAL ASSAULT'])
        csa_norms.append(norm['CRIM SEXUAL ASSAULT'])
    except Exception:
        csa_values.append(0)
        csa_norms.append(0)
    try:
        nocrim_values.append(val['NON-ASSAULT'])
        nocrim_norms.append(norm['NON-ASSAULT'])
    except Exception:
        nocrim_values.append(0)
        nocrim_norms.append(0)

# Column titles for DataFrame (matches primary_type)        
crimes = 'THEFT', 'DECEPTIVE PRACTICE', 'CRIMINAL TRESPASS', 'BATTERY', 'CRIMINAL DAMAGE', 'ASSAULT', 'PROSTITUION', 'NARCOTICS', 'ROBBERY', 'PUBLIC PEACE VIOLATION', 'BURGLARY', 'LIQUOR LAW VIOLATION', 'INTERFERENCE WITH PUBLIC OFFICER', 'HOMICIDE', 'CRIMINAL SEXUAL ASSAULT', 'MOTOR VEHICLE THEFT', 'ARSON', 'SEX OFFENSE', 'INTIMITDATION', 'WEAPONS VIOLATION', 'OFFENSE INVOLVING CHILDREN', 'PUBLIC INDECENCY', 'STALKING', 'KIDNAPPING', 'CONCEALED CARRY LICENSE VIOLATION', 'OBSCENITY', 'CRIM SEXUAL ASSAULT', 'NON-CRIMINAL', 'OTHER OFFENSE'

# Value_count() integer data     
values_data = (theft_values, decpra_values, tres_values, batt_values, dam_values, assault_values, prost_values, narc_values, 
               robb_values, ppv_values, burg_values, llv_values, iwpo_values, homi_values, sa_values, mvtheft_values, 
               arson_values, so_values, intim_values, wv_values, oic_values, pi_values, stalk_values, kidn_values, cclv_values, 
               obs_values, csa_values, nocrim_values, other_values)

# Value_count() normalized (percentage) data   
norms_data = (theft_norms, decpra_norms, tres_norms, batt_norms, dam_norms, assault_norms, prost_norms, narc_norms, robb_norms, 
              ppv_norms, burg_norms, llv_norms, iwpo_norms, homi_norms, sa_norms, mvtheft_norms, arson_norms, so_norms, 
              intim_norms, wv_norms, oic_norms, pi_norms, stalk_norms, kidn_norms, cclv_norms, obs_norms, csa_norms, 
              nocrim_norms, other_norms)

# Integer DataFrame
valuesDF = pandas.DataFrame(values_data, columns = years)
valuesDF['Crime'] = crimes
valuesDF = valuesDF.set_index('Crime')

# Normalized DataFrame
normsDF = pandas.DataFrame(norms_data, columns = years)
normsDF['Crime'] = crimes
normsDF = normsDF.set_index('Crime')

print(valuesDF)
print(normsDF)

#Tom's code 
gdp_data_df = pandas.read_csv('./SourceData/GDP_year.csv')
crime_df = pandas.read_csv('./output/All_CrimeData.csv')

crime_counts=crime_df.groupby(["year"]).count()["id"]
crime_gdp_df=pandas.DataFrame({'year':crime_counts.index, "crime counts":crime_counts.values, "GDP":gdp_data_df["GDP"]})
#crime_gdp_df=crime_gdp_df.drop(19)
plt.scatter(crime_gdp_df["crime counts"],crime_gdp_df["GDP"])
plt.title("Correlation Between Crime Count and GDP")
plt.xlabel('Crime Count per Year')
plt.ylabel('Measure of Yearly GDP')
plt.show()

crimes = crime_gdp_df["crime counts"]
gdp = crime_gdp_df["GDP"]
correlation = st.pearsonr(crimes,gdp)
print(f"The correlation between crime and GDP is {round(correlation[0],2)}")