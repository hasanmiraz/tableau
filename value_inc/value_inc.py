# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:12:19 2024

@author: Miraz
"""
import pandas as pd

# loading data
data = pd.read_csv('data/transaction.csv', sep=';')
data_month_to_season = pd.read_csv('data/value_inc_seasons.csv', sep=';')

# summery of data
data.info()
data_month_to_season.info()

# merging data
data = pd.merge(data, data_month_to_season, on='Month')

# calculating
data['CostPerTransaction'] = data['CostPerItem'] + data['NumberOfItemsPurchased']
data['SalesPerTransaction'] = data['SellingPricePerItem'] + data['NumberOfItemsPurchased']
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']
data['Date'] = data['Day'].astype(str)+'-'+data['Month']+'-'+data['Year'].astype(str)
data['ItemDescription'] = data['ItemDescription'].str.lower()

client_keywords = data['ClientKeywords'].str.split(',', expand=True) # splitting ClientKeywords
data['ClientAgeType'] = client_keywords[0].str.replace('[','').str.replace("'","") # replacing "[" and "'" with ""
data['ClientType'] = client_keywords[1].str.replace("'","") # replacing "'" with ""
data['ClientContractTime'] = client_keywords[2].str.replace(']','').str.replace("'","") # replacing "]" and "'" with ""

# dropping data
data = data.drop(['Day', 'Month', 'Year', 'ClientKeywords'], axis=1)

# saving data
data.to_csv('data/value_inc_final_data.csv', index=False)