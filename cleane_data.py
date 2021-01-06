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



#job title domain expertise (Product, Finance etc.)
#job title seniority expertise (Junior, Senior etc.)


#company age
#tech stack per role parcing

#remove nulls
df = df[df['Salary Estimate']!= '-1']


#salary parcing
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
replace_p_k = salary.apply(lambda x: x.replace('£', '').replace('K', ''))

df['min_salary'] = replace_p_k.apply(lambda x: int(x.split(' ')[0])) 
df['max_salary'] = replace_p_k.apply(lambda x: int(x.split(' ')[-2]))
df['avg_salary'] = (df.min_salary+df.max_salary)/2       
                         
#company name text only
df['company_name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

#city
df['city'] = df['Location'].apply(lambda x: x.split(',')[0])

#company age










