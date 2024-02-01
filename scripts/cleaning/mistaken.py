import pandas as pd
import numpy as np

def mistakendata():
    df = pd.read_csv("Dataset.csv")
    print("Valores únicos que toma la variable antes:", df['Dependent_count'].unique())
    df['Dependent_count'] = df['Dependent_count'].replace(-1, np.nan)
    print("Valores únicos que toma la variable despues:", df['Dependent_count'].unique())
    df.to_csv("Dataset.csv", index=False)

if __name__ == "__main__":
    mistakendata()
