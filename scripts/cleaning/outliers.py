"""
Outliers
"""
import os
import seaborn as sns
import matplotlib.pyplot as plt


def outliersfunction(df_to_clean):
    """
    Remove outliers from the DataFrame
    """
    if not os.path.exists("outliers/before"):
        os.makedirs("outliers/before")
    if not os.path.exists("outliers/after"):
        os.makedirs("outliers/after")

    for column in df_to_clean.columns:
        if df_to_clean[column].dtype != "object":
            q1 = df_to_clean[column].quantile(0.25)
            q3 = df_to_clean[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 30 * iqr
            upper_bound = q3 + 30 * iqr
            outliers = df_to_clean[
                (df_to_clean[column] < lower_bound
                 ) | (df_to_clean[column] > upper_bound)]

            if not outliers.empty:
                sns.boxplot(x=df_to_clean[column]).set_title(
                    f"Before Cleaning - {column}")
                plt.savefig(f"outliers/before/{column}_before.png")
                plt.clf()

                sns.boxplot(x=df_to_clean[~df_to_clean.index.isin(
                    outliers.index)][column]).set_title(
                        f"After Cleaning - {column}")
                plt.savefig(f"outliers/after/{column}_after.png")

    print("Outliers removal completed. Images saved in 'outliers'.")
    return df_to_clean
