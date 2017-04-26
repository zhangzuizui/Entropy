#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:29:20 2017

@author: zzzzzui
"""
import os
import pandas as pd 
import datetime

def SetDummies(aDatetime, time_interval=3):
    
    dt = datetime.datetime.strptime(aDatetime, '%Y-%m-%d %H:%M:%S')
    
    return int(dt.hour/time_interval)


path = os.getcwd() + '/' + 'time_preference'
for filename in os.listdir(path):
    file = pd.read_csv(path+'/'+filename, dtype=str, index_col='Unnamed: 0')
    filegroup = file.groupby(['USER_ID'])
    print(filegroup.sum())
    