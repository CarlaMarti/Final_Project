import click
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def outliersfunction(df_to_clean):

    if not os.path.exists('outliers/before'):
        os.makedirs('outliers/before')
    if not os.path.exists('outliers/after'):
        os.makedirs('outliers/after')
    for column in df_to_clean.columns:
        if df_to_clean[column].dtype != 'object':  # Solo trabajar con variables numéricas
            Q1 = df_to_clean[column].quantile(0.25)
            Q3 = df_to_clean[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 50 * IQR
            upper_bound = Q3 + 50 * IQR
            outliers = df_to_clean[(df_to_clean[column] < lower_bound) | (df_to_clean[column] > upper_bound)]

            if not outliers.empty: 
                sns.boxplot(x=df_to_clean[column]).set_title(f'Before Cleaning - {column}')
                plt.savefig(f'outliers/before/{column}_before.png')
                plt.clf()

                sns.boxplot(x=df_to_clean[~df_to_clean.index.isin(outliers.index)][column]).set_title(f'After Cleaning - {column}')
                plt.savefig(f'outliers/after/{column}_after.png')
    
        print("Outliers detection and removal completed. Images saved in 'outliers' folder.")
        return df_to_clean

