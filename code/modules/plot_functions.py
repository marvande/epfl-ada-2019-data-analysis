#imports: 
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import os
import seaborn as sns
from scipy import stats

"""
cat_count_plot: plots the number of occurences per category in to_be_plotted.

@input: 
- to_be_plotted: categorical data (e.g. columns of incomes for all households)
- title: the title we want to give the plot

@output: plots the number of occurences per category
"""
def cat_count_plot(to_be_plotted, title):
    fig, axs = plt.subplots(1,1, figsize = (18,6))

    sns.countplot(to_be_plotted, ax = axs)

    axs.set_xticklabels(axs.get_xticklabels(), rotation = 45, horizontalalignment = 'right')
    axs.set(title = title)

"""
plot_box_dist: plots the boxplot and distribution of an entered series. 

@input: 
- to_be_plotted: panda series from which we want to plot the distribution and boxplot
- title: title we want to give the plot
- xlabel: label for x axis

@output: see above. 
"""
def plot_box_dist(to_be_plotted, title, xlabel):
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

"""
double_plot_box_dist: does a double box plot with distribution with a shared x axis. 
@input:
- to_be_plotted1, to_be_plotted2: panda series from which we want to plot the distribution and boxplot
- titles = array of titles to give both plots
- xlabels = array of labels for both xaxis

@output: see above. 
"""
def double_plot_box_dist(to_be_plotted1, to_be_plotted2, titles, xlabels):
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

"""
double_categorical_scatter: does a double categorical scatter plot. 
@input: 
- to_be_plotted1x, to_be_plotted1y: data for first categorical scatter plot
- to_be_plotted2x, to_be_plotted2y: data for second categorical scatter plot
- titles = array of titles for plots
- add_mean = True if we want to add the mean on the plots. 

@output: see above. 
"""
def double_categorical_scatter(to_be_plotted1x, to_be_plotted1y, to_be_plotted2x, to_be_plotted2y, titles, add_mean = False):
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
