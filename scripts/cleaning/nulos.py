import pandas as pd

def eliminar_nulos():
    df = pd.read_csv("Dataset.csv")
    print("Valores nulos antes: \n",df.isnull().sum(),"\n\n\n")
    numeric_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(exclude=['number']).columns

    for column in numeric_columns:
        df[column].fillna(df[column].mean(), inplace=True)

    df.dropna(subset=categorical_columns, inplace=True)
    
    print("Valores nulos despues: \n",df.isnull().sum(),"\n")
    df.to_csv("Dataset.csv", index=False)

if __name__ == "__main__":
    eliminar_nulos()
