#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:09:59 2021

@author: andrii
"""

import selenium_scrapping_script as sss
import pandas as pd 
path = "/Users/andrii/Documents/Git/ds_job_search_project/chromedriver"

df = sss.get_jobs('data analyst', 1200, False, path, 15)
df
