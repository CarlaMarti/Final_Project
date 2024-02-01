import click
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

@click.command()
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
def outliersfunction(out):
    if out:
        df = pd.read_csv('Dataset.csv')

        if not os.path.exists('outliers/before'):
            os.makedirs('outliers/before')
        if not os.path.exists('outliers/after'):
            os.makedirs('outliers/after')

        for column in df.columns:
            if df[column].dtype != 'object':  # Solo trabajar con variables numéricas
                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 50 * IQR
                upper_bound = Q3 + 50 * IQR

                outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

                if not outliers.empty: 
                    sns.boxplot(x=df[column]).set_title(f'Before Cleaning - {column}')
                    plt.savefig(f'outliers/before/{column}_before.png')
                    plt.clf()

                    sns.boxplot(x=df[~df.index.isin(outliers.index)][column]).set_title(f'After Cleaning - {column}')
                    plt.savefig(f'outliers/after/{column}_after.png')
                    plt.clf()

        print("Outliers detection and removal completed. Images saved in 'outliers' folder.")
    else:
        print("No action taken. Please use '-out' flag to detect and remove outliers.")

if __name__ == '__main__':
    outliersfunction()
