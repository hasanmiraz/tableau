# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:48:01 2024

@author: Miraz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read file
data = pd.read_json('data/loan_data_json.json')

# summery of data
data.info()

# calculations
data['annual.income'] = np.exp(data['log.annual.inc'])

fico_category = []
for fico in data['fico']: 
    try:
        if fico >= 300 and fico < 400:
            fico_category.append('Very Poor')
        elif fico >= 400 and fico < 600:
            fico_category.append('Poor')
        elif fico >= 600 and fico < 660:
            fico_category.append('Fair')
        elif fico >= 660 and fico < 780:
            fico_category.append('Good')
        elif fico >= 780 and fico:
            fico_category.append('Excellent')
        else:
            print('here')
            fico_category.append('Unknown')
    except:
        fico_category.append('Unknown')
data['fico.category'] = pd.Series(fico_category)

data.loc[data['int.rate'] > 0.12, 'interest.type'] = "high"
data.loc[data['int.rate'] <= 0.12, 'interest.type'] = "low"

# ploting data
fico_category_plot = data.groupby('fico.category').size()
fico_category_plot.plot.bar(color = 'red', width = 0.1)
plt.show()

perpose_plot = data.groupby('purpose').size()
perpose_plot.plot.bar(color = 'orange', width = .2)
plt.show()

plt.scatter(data['dti'], data['annual.income'], color = 'black')
plt.show()