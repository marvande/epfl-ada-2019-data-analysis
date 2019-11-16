#Functions used with the demographic dataframe. 

#imports: 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import os
import seaborn as sns
from scipy import stats

"""
order_hh_dem: renders a column in the demographic dataframe categorical according to a specific ordering. 
@input: 
- hh_dem: demographic dataframe
- label: column name
- ordered_label: ordering for the categorical variables
"""
def order_hh_dem(hh_dem, label, ordered_label):
    ordered_column = pd.Categorical(hh_dem[label],
                      ordered = True,
                      categories = ordered_label)
    return ordered_column 

