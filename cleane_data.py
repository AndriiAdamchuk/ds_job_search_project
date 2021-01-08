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


#remove nulls, duplicates, and Unnamed column
df = df.drop_duplicates()
df = df[df['Salary Estimate']!= '-1']
df = df.drop(['Unnamed: 0'], axis = 1)


#job title cleaning (Data Analyst, BI Analyst, etc.)
def clean_title(title):
    if 'business analyst ' in title.lower(): 
        return 'business analyst'
    elif 'data analyst' in title.lower() or 'data insights analyst' in title.lower():
        return 'data analyst'
    else:
        return 'na'
    
df['job_title_short'] = df['Job Title'].apply(clean_title)


#job title seniority expertise (Junior, Senior, etc.)
def title_seniority(title):
    if 'junior' in title.lower() or 'jr' in title.lower() or 'jr.' in title.lower():
        return 'junior'
    elif 'senior' in title.lower() or 'sr' in title.lower() or 'sr.' in title.lower():
        return 'senior'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'lead' in title.lower():
        return 'lead'
    else:
        return 'na'

df['seniority'] = df['Job Title'].apply(title_seniority)


#job title domain expertise (Product, Finance etc.)
def expertize(title):
    if 'people' in title.lower() or 'hr' in title.lower():
        return 'hr'
    elif 'marketing' in title.lower() or 'user acquisition' in title.lower():
        return 'marketing'
    elif 'finance' in title.lower() or 'fintech' in title.lower():
        return 'finance'
    elif 'crm' in title.lower():
        return 'crm'
    elif 'product' in title.lower():
        return 'product'
    elif 'project' in title.lower():
        return 'project'
    elif 'retail' in title.lower():
        return 'retail'
    elif 'sales' in title.lower():
        return 'sales'
    else:
        return 'other'

df['business_domain'] = df['Job Title'].apply(expertize)


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
df['company_age'] = df['Founded'].apply(lambda x: (2021 - x) if x >0 else x)


#parcing tech stack per role

#sql
df['sql_yn'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r studio
df['r_yn'] = df['Job Description'].apply(lambda x: 1 if ' r ' in x.lower() else 0)

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#tableau
df['tableau_yn'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)

#powerbi
df['powerbi_yn'] = df['Job Description'].apply(lambda x: 1 if 'powerbi' in x.lower() else 0)

#kafka
df['kafka_yn'] = df['Job Description'].apply(lambda x: 1 if 'kafka' in x.lower() else 0)

#snowflake
df['snowflake_yn'] = df['Job Description'].apply(lambda x: 1 if 'snowflake' in x.lower() else 0)

df.to_csv("df_final.csv", index = False)