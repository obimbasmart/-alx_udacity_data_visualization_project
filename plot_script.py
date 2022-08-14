

import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import rcParams


#create a function for creating bars
# get the order index
#group the data using value_count
#get the total data

#plot the data
#########loooooooooooooop

def create_relative_frequency(data, column, n_subset=10, plot_frequency=True):
    '''
        This function takes a dataframe and a categorical column, and plots
        a bar chart with proper annotation and style
    '''
    #group the data using value_count
    grouped_value_count = data[column].value_counts(dropna=True)
    top_n_index = grouped_value_count[:n_subset].index
    top_n = data[data[column].isin(top_n_index)]
    
    #plot the data
    rcParams['figure.figsize'] = 16,4
    g = sb.countplot(data=top_n, x = column, color=sb.color_palette()[0], order=top_n_index);
    ylabels = ['{:,.0f}'.format(x) + 'K' for x in g.get_yticks()/1000]
    g.set_yticklabels(ylabels)
    plt.locator_params(axis='y', nbins=4)
    sb.despine(bottom = True, left = False)
    plt.margins(0.02, 0.1)
    
    if plot_frequency:
        ####loooooooooooop
        locs, labels = plt.xticks(rotation=90)
        for loc, label in zip(locs, labels):

            # get the text property for the label to get the correct count
            count = grouped_value_count[label.get_text()]
            pct_string = '{:0.1f}%'.format(100*count/grouped_value_count.sum())

            # print the annotation just below the top of the bar
            plt.text(loc, count+2, pct_string, ha = 'center', color = 'black')
        
def plot_value_count(data, column):
    ''' This function takes a dataframe and a categorical column name, and
        plots a barplot of relative frequency for each category in the column
        
        Args: DataFrame, column: string
        return: a seaborn plot axis object'''
    
    count = data[column].value_counts(normalize=True)
    x = count.index
    y = count.values
    rcParams['figure.figsize'] = 16,4
    g = sb.barplot(x=x, y=y, color=sb.color_palette()[0])
    sb.despine(bottom = True, left = False)
    plt.margins(0.02, 0.1)
    
    plt.yticks(g.get_yticks(), ['{:,.1f}%'.format(x*100) for x in g.get_yticks()]);
    return g