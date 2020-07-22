# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:55:06 2020

@author: lakshay
"""


import pandas as pd
dataset=pd.read_excel("3. Descriptive Statistics.xlsx",sheet_name=0)
from scipy.stats import pearsonr
stats,p=pearsonr(dataset.JobCategory, dataset.CurrentSalary)
print(p)
#As our alternative hypothesis comes true from the value of p,so we can say that 
#there is a significant correlation between JobCategory and CurrentSalary.

import matplotlib.pyplot as pyt
pyt.scatter(dataset.JobCategory,dataset.CurrentSalary)
#It is also clear from the graph
print(dataset.corr())
#The vaule of r between JobCategory and CurrentSalary is .78 which is strongly positive.