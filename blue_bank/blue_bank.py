# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:48:01 2024

@author: Miraz
"""

import pandas as pd

# read file
data = pd.read_json('data/loan_data_json.json')

# summery of data
data.info()