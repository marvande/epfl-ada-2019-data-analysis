#Functions used with the demographic dataframe. 

#imports: 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import os
import seaborn as sns
from scipy import stats


def order_hh_dem(hh_dem, label, ordered_label):
    """
    Renders a column in the demographic dataframe categorical according to a specific ordering. 
    @input: 
    - [pd.DataFrame] hh_dem: demographic dataframe
    - [string] label: column name
    - [list of string] ordered_label: ordering for the categorical variables
    @output: outputs a pd.Categorical ordered column. 
    """
    ordered_column = pd.Categorical(hh_dem[label],
                      ordered = True,
                      categories = ordered_label)
    return ordered_column 

