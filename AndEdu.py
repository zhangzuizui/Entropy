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
            self.arr = np.array(self.aDF)
            self.shape = list(self.arr.shape)
            
    def covariance(self, arrA, arrB):
        
        SUM = 0
        n = self.shape[1]
        avgA = sum(arrA)/n
        avgB = sum(arrB)/n
        
        for i in range(n):
            SUM += (arrA[i]-avgA) * (arrB[i]-avgB)
            
        return SUM/n
        
        
    
    def PearsonCor(self):
        
        LEN = self.shape[1]
        ans = np.zeros([LEN, LEN])
        
        for i in range(LEN):            
            ans[i, i] = 1                                    
            for j in range(i+1, LEN):                
                #computing pearson correlation
                ans[i, j] = self.covariance(self.arr[:,[i]].T[0], self.arr[:,[j]].T[0]) / (
                        np.std(self.arr[:,[i]].T[0])*np.std(self.arr[:,[j]].T[0]))
                ans[j, i] = ans[i, j]
                
        #return a pearson correlation matrix
        return ans

#to do negative
    def RegularScale(self):
        
        arr_log = np.log(self.arr + np.ones(self.shape)) 
        Positive_matrix = np.zeros(self.shape)
        
        for j in range(self.shape[1]):
            for i in range(self.shape[0]):
                Positive_matrix[i][j] = (arr_log[i][j]-min(arr_log[:, [j]].T[0])) / (
                        max(arr_log[:, [j]].T[0]) - min(arr_log[:, [j]].T[0]))
        
        return Positive_matrix
    
    def Frequency(self):
        
        X = self.RegularScale()
        f = np.zeros(self.shape)
        
        for j in range(self.shape[1]):
            for i in range(self.shape[0]):
                f[i][j] = X[i][j] / sum(X[:, [j]].T[0])
        
        return f
        
        
        
    
    def Entropy(self):
        
        X = self.Frequency()
        e = np.zeros(self.shape[1])
        m = self.shape[0]
        
        for j in range(self.shape[1]):
            molecular = 0
            for i in range(m):
                if X[i][j] == 0:
                    pass
                else:
                    molecular += X[i][j] * np.log(X[i][j])
            e[j] = - molecular / np.log(m)
        
        return e
    
    def Weight(self):
        
        e = self.Entropy()
        w = np.zeros(len(e))
        denominator = sum(np.ones(len(e)) - e)
       
        for j in range(len(e)):
            w[j] = (1 - e[j]) / denominator
        
        return w
        
        