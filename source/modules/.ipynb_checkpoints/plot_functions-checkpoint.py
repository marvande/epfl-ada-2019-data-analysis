#imports: 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import os
import seaborn as sns
from scipy import stats


def cat_count_plot(to_be_plotted, title):
    """
    Plots the number of occurences per category in to_be_plotted.
    @input: 
    - [pd.Series] to_be_plotted: categorical data (e.g. columns of incomes for all households)
    - [string] title: the title we want to give the plot
    @output: plots the number of occurences per category
    """
    fig, axs = plt.subplots(1,1, figsize = (18,6))

    sns.countplot(to_be_plotted, ax = axs)

    axs.set_xticklabels(axs.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
    axs.set(title = title)

def corr_function_plot(x, y, **kwargs):
    """
    Function used in pair_corr_plot. Calculates the correlation between 2 variables and adds it on the scatter plot. 
    @input: 
    - [continuous variable] x: first variable
    - [continuous variable] y: second variable
    - **kwargs: additional arguments for function plotting 
    @output: see above. 
    """ 
    # Calculate the value: 
    coef = np.corrcoef(x, y)[0][1]
    # Make the label: 
    label = r'$\rho$ = ' + str(round(coef, 2))
    
    # Add the label to the plot: 
    ax = plt.gca()
    ax.annotate(label, xy = (0.2, 1), size = 10, xycoords = ax.transAxes)
    
    
def double_categorical_scatter(to_be_plotted1x, to_be_plotted1y, to_be_plotted2x, to_be_plotted2y, titles, add_mean = False):
    """
    Does a double categorical scatter plot. 
    @input: 
    - [pd.Series] to_be_plotted1x, to_be_plotted1y: x and y axis for first categorical scatter plot
    - [pd.Series] to_be_plotted2x, to_be_plotted2y: x and y axis  for second categorical scatter plot
    - [array of string] titles = array of titles for plots
    - [Boolean] add_mean = True if we want to add the mean on the plots

    @output: double categorical scatter plot.  
    """
    fig, axs = plt.subplots(1,2, figsize = (18,6))
    
    sns.swarmplot(x = to_be_plotted1x, y = to_be_plotted1y, ax = axs[0])
    if add_mean: 
        axs[0].axhline(to_be_plotted1y.mean(), color = 'r', linestyle = '--')
    
    sns.swarmplot(x = to_be_plotted2x, y = to_be_plotted2y, ax = axs[1])
    if add_mean: 
        axs[1].axhline(to_be_plotted2y.mean(), color = 'r', linestyle = '--')
        plt.legend({'Mean': mean})
    
    #Rotate labels: 
    axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation = 45, horizontalalignment = 'right')
    axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation = 45, horizontalalignment = 'right')

    axs[0].set(title = titles[0])
    axs[1].set(title =  titles[1])

    
def double_plot_box_dist(to_be_plotted1, to_be_plotted2, titles, xlabels):
    """
    Does a double box plot with distribution with a shared x axis. 
    @input:
    - [pd.Series] to_be_plotted1, to_be_plotted2: panda series from which we want to plot the distribution and boxplot
    - [list of string] titles = array of titles to give both plots
    - [list of string] xlabels = array of labels for both xaxis

    @output: boxplot and distribution of to_be_plotted1 and to_be_plotted2
    """
    f, axes = plt.subplots(2, 2, sharex = 'col', gridspec_kw = {"height_ratios": (0.2, 2)}, figsize = (20,8))
    
    means = [to_be_plotted1.mean(), to_be_plotted2.mean()]
    medians = [to_be_plotted1.median(), to_be_plotted2.median()]
    
    sns.boxplot(to_be_plotted1, ax = axes[0,0])
    axes[0,0].axvline(means[0], color = 'r', linestyle = '--')
    axes[0,0].axvline(medians[0], color = 'g', linestyle = '-')

    sns.distplot(to_be_plotted1, ax = axes[1,0])
    axes[1,0].axvline(means[0], color = 'r', linestyle = '--')
    axes[1,0].axvline(medians[0], color = 'g', linestyle = '-')

    sns.boxplot(to_be_plotted2, ax =axes[0,1])
    axes[0,1].axvline(means[1], color = 'r', linestyle = '--')
    axes[0,1].axvline(medians[1], color = 'g', linestyle = '-')

    sns.distplot(to_be_plotted2, ax = axes[1,1])
    axes[1,1].axvline(means[1], color = 'r', linestyle = '--')
    axes[1,1].axvline(medians[1], color = 'g', linestyle = '-')

    plt.legend({'Mean':mean,'Median':median})

    axes[0,0].set(xlabel = '', title = titles[0])
    axes[0,1].set(xlabel = '', title = titles[1])

    axes[1,0].set(xlabel = xlabels[0])
    axes[1,1].set(xlabel = xlabels[1])

    plt.show()

def pair_corr_plot(to_be_plotted, correlation_function = corr_function_plot, hue = None):
    """
    Plots a pair plot with the scatter plots and correlation coefficients off diagonal, and histograms on the diagonal. 
    @input: 
    - [pd.DataFrame] to_be_plotted : the dataframe with each column being one variable. 
    - [function] correlation_function : the correlation function which is used 
    @output: see above. 
    """ 
    fig = sns.pairplot(to_be_plotted, hue)
    fig = fig.map_offdiag(correlation_function)
    
def pie_plot_labels(df):
    #Look at proportions:
    medians = []

    labels = ['VEGETABLES_QUANT', 'FRUIT_QUANT',
       'MEAT & SEAFOOD_QUANT', 'HOUSEHOLDS_QUANT',
       'COOKIES SNACKS & CANDY _QUANT', 'CONDIMENTS/SPICES & BAKE_QUANT',
       'DAIRY_QUANT', 'BEVERAGES_QUANT']

    for label in labels:
        medians.append(df[label].median())

    #add colors
    colors = ['#800026','#bd0026','#e31a1c','#fc4e2a','#fd8d3c','#feb24c','#fed976',
    '#ffeda0','#ffffcc']   

    medians = pd.Series(index = labels, data = medians,)

    #explsion
    explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05)
    fig, ax1 = plt.subplots(1,1)
    ax1.pie(medians, labels = labels,autopct='%1.1f%%', colors = colors,startangle=90, pctdistance=0.85, explode = explode)
    #draw circle
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax1.axis('equal')  
    plt.tight_layout()
    plt.show()
    
    
def plot_box_dist(to_be_plotted, title, xlabel):
    """
    Plots the boxplot and distribution of an entered series with shared x axis. 
    @input: 
    - [pd.Series] to_be_plotted: series from which we want to plot the distribution and boxplot
    - [string] title: title we want to give the plot
    - [string] xlabel: label for x axis

    @output: boxplot and distribution of to_be_plotted
    """
    f, axes = plt.subplots(2, 1, sharex = 'col', gridspec_kw = {"height_ratios": (0.2, 2)}, figsize = (5,5))
    
    mean = to_be_plotted.mean()
    median = to_be_plotted.median()
    
    sns.boxplot(to_be_plotted, ax = axes[0])
    axes[0].axvline(mean, color = 'r', linestyle='--')
    axes[0].axvline(median, color = 'g', linestyle='-')

    sns.distplot(to_be_plotted, ax = axes[1])
    axes[1].axvline(mean, color = 'r', linestyle='--')
    axes[1].axvline(median, color = 'g', linestyle='-')

    plt.legend({'Mean':mean,'Median':median})

    axes[0].set(xlabel = '', title = title)
    axes[1].set(xlabel = xlabel)

    plt.show()    

def plot_demographics(hh_demographic_fxd):
    """
    Plots the number of households per category for the household dataframe.
    @input:
    - [pd.DataFrame] hh_demographic_fxd: dataframe with household data
    
    @output: categorical histograms for each category
    """
    fig, axs = plt.subplots(2, 3, figsize=(18, 13))

    sns.countplot(hh_demographic_fxd['AGE_DESC'], ax=axs[0, 0])

    sns.countplot(hh_demographic_fxd['MARITAL_STATUS_CODE'], ax=axs[0, 1])

    sns.countplot(hh_demographic_fxd['INCOME_DESC'], ax=axs[1, 0])
    axs[1, 0].set_xticklabels(axs[1, 0].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['HOMEOWNER_DESC'], ax=axs[1, 1])
    axs[1, 1].set_xticklabels(axs[1, 1].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['KIDS_DESC'], ax=axs[1, 2])
    axs[1, 2].set_xticklabels(axs[1, 2].get_xticklabels(),
                              rotation=45,
                              horizontalalignment='right')

    sns.countplot(hh_demographic_fxd['HOUSEHOLD_SIZE_DESC'], ax=axs[0, 2])


    plt.show()
