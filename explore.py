

# imports
import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import wrangle
import warnings
warnings.filterwarnings('ignore')




def plot_variable_pairs(df):
    '''
    Takes in a dataframe and returns plots of all pariwise relationships with the regression line for each pair.
    
    '''    
    g=sns.PairGrid(df)
    g.map_diag(plt.hist)
    g.map_offdiag(sns.regplot)
    
#     sns.set(style='ticks', context='talk')
#     plt.style.use('fast')
#     sns.pairplot(df_sample, kind='reg', plot_kws={'scatter_kws': {'s': 1, 'color': 'lightcoral'}})
    plt.show()







def plot_categorical_and_continuous_vars(df, cat_cols, con_cols):
    """
    Plot three different visualizations for the relationship between
    categorical variables and continuous variables.

    Parameters:
    - df: DataFrame, the input dataframe.
    - cat_cols: list, names of columns holding categorical variables.
    - con_cols: list, names of columns holding continuous variables.
    """

    
    for cat_var in cat_cols:
        for con_var in con_cols:

            # Plot 1: Boxplot
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 3, 1)
            sns.boxplot(x=cat_var, y=con_var, data=df)
            plt.title(f'Boxplot of {con_var} by {cat_var}')

            # Plot 2: Violin plot
            plt.subplot(1, 3, 2)
            sns.violinplot(x=cat_var, y=con_var, data=df)
            plt.title(f'Violin Plot of {con_var} by {cat_var}')

            # Plot 3: hist plot 
            plt.subplot(1, 3, 3)
            for category in df[cat_var].unique():
                sns.histplot(df[df[cat_var] == category][con_var], label=category, alpha=0.5, kde=True)
            plt.title(f'Histogram of {con_var} by {cat_var}')
            plt.legend()

            plt.tight_layout()
            plt.show()






