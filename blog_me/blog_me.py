# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:46:43 2024

@author: Miraz
"""

import pandas as pd

# read files
data = pd.read_excel('data/articles.xlsx')

# summery of data
data.info()

# count the necessary fields
data.groupby(['source_id'])['article_id'].count() # counting articales from unique sources
data.groupby(['source_id'])['engagement_reaction_count'].sum() # counting total likes from unique sources
data.groupby(['source_id'])['engagement_comment_count'].sum() # counting total comments from unique sources
data.groupby(['source_id'])['engagement_share_count'].sum() # counting total shares from unique sources
