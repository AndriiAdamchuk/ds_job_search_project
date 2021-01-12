#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 21:11:06 2021

@author: andrii
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('df_eda.csv')

# choose relevant columns
df.columns
df_model = df[['avg_salary', 'Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue', 'job_title_short', 'seniority',
             'business_domain', 'city', 'company_age', 'sql_yn', 'python_yn', 'r_yn','spark_yn', 'aws_yn', 'excel_yn', 
             'tableau_yn', 'powerbi_yn', 'kafka_yn', 'snowflake_yn', 'description_len']]

# get dummy variables
df_dum = pd.get_dummies(df_model)


# train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('avg_salary', axis = 1)
y = df_dum.avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# multiple linear regression (statsmodels and sklearn to compare them)
import statsmodels.api as sm 

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary() 

    # P>|t| focusing on features with value <0.05  
    # Excel knowledge featured in job position adds 2K more
    # if the company size from 1001 to 5000 employees they usually pay 7K more
    # Banks & Credit Unions paying 17K more
    # Federal Agencies paying 11K less
    # Industrial Manufacturing paying 15K less
    # Transportation Management paying 14K less
    # Companies with revenue of $500 million to $1 billion paying 7K more
    # Job title business analyst +8K more/ data analyst +4K more
    # Manager seniority +27K more
    # Openings in London offers +4K more / in city_Egham +20K more

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3))
 

# random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv=3))


# tune models GridsearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse', 'mae'), 'max_features':('auto', 'sqrt', 'log2')}

gs = GridSearchCV(rf,parameters,scoring = 'neg_mean_absolute_error', cv=3)  
gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# test ensambles
tpred_lm = lm.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_rf)
mean_absolute_error(y_test,(tpred_rf+tpred_lm)/2)

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

#model.predict(X_test.iloc[1,:].values.reshape(1,-1))