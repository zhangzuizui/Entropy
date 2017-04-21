#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 16:13:06 2017

@author: zzzzzui
"""

import pandas as pd
from pandas import DataFrame, Series
import numpy as np

class AndEdu(object):
    
    def __init__(self, aDF):
        
        if type(aDF) != DataFrame:
            raise ValueError('Initialize this class with a DataFrame')
        else:
            self.aDF = aDF
            
    def covariance(arrA, arrB):
        
        SUM = 0
        n = len(arrA)
        avgA = sum(arrA)/n
        avgB = sum(arrB)/n
        
        for i in range(n):
            SUM += (arrA[i]-avgA) * (arrB[i]-avgB)
            
        return SUM/n     
        
        
    
    def PearsonCor(self):
        
        LEN = len(self.aDF.columns)
        arr = np.array(self.aDF)
        ans = np.zeros([LEN, LEN])
        
        for i in range(LEN):            
            ans[i, i] = 1                                    
            for j in range(i+1, LEN):                
                #computing pearson correlation
                ans[i, j] = np.cov(arr[:,[i,j]].T) / (np.std(arr[:,[i]].T)*np.std(arr[:,[j]].T))
                ans[j, i] = ans[i, j]
                
                np.correlate
        #return a pearson correlation matrix
        return ans
    
    
                
        
        