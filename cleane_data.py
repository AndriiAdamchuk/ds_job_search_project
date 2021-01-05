#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 23:04:20 2021

@author: andrii
"""

import pandas as pd

df1 = pd.read_csv('df_glasdoor_1.csv') 
df2 = pd.read_csv('df_glasdoor_2.csv') 
df3 = pd.read_csv('df_glasdoor_3.csv') 
df4 = pd.read_csv('df_glasdoor_4.csv') 

df = pd.concat([df1, df2, df3, df4])

#remove nulls
#job title domain expertise (Product, Finance etc.)
#job title seniority expertise (Junior, Senior etc.)
#salary parcing
#company name text only
#citysal
#company age
#tech stack per role parcing

df = df[df['Salary Estimate']!= '-1']