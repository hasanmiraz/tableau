# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 18:46:43 2024

@author: Miraz
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# read files
data = pd.read_excel('data/articles.xlsx')

# summery of data
data.info()

# count the necessary fields
data.groupby(['source_id'])['article_id'].count() # counting articales from unique sources
data.groupby(['source_id'])['engagement_reaction_count'].sum() # counting total likes from unique sources
data.groupby(['source_id'])['engagement_comment_count'].sum() # counting total comments from unique sources
data.groupby(['source_id'])['engagement_share_count'].sum() # counting total shares from unique sources

# dropping column
data = data.drop('engagement_comment_plugin_count', axis = 1)

# keyword flagging

keywords = ['crash', 'murder', 'attack']
keyword_flag = []
for title in data['title']:
    try:
        if len([word for word in keywords if word in title])>0 :
            keyword_flag.append(1)
        else:
            keyword_flag.append(0)
    except:
        keyword_flag.append(0)
data['keyword_flag'] = pd.Series(keyword_flag)

# sentiment analyzing
sent_analyzer = SentimentIntensityAnalyzer()

title_positive_sentiment = []
title_negative_sentiment = []
title_neutral_sentiment = []

for title in data['title']:
    try:
        sentiment = sent_analyzer.polarity_scores(title)
        title_positive_sentiment.append(round(sentiment['pos'], 2))
        title_negative_sentiment.append(round(sentiment['neg'], 2))
        title_neutral_sentiment.append(round(sentiment['neu'], 2))
    except:
        title_positive_sentiment.append(0)
        title_negative_sentiment.append(0)
        title_neutral_sentiment.append(0)
data['title_positive_sentiment'] = pd.Series(title_positive_sentiment)
data['title_negative_sentiment'] = pd.Series(title_negative_sentiment)
data['title_neutral_sentiment'] = pd.Series(title_neutral_sentiment)

# saving file as xlsx
data.to_excel('data/blog_me_final.xlsx', sheet_name = "BlogMe", index = False)
data.to_csv('data/blog_me_final.csv', index = False)



















