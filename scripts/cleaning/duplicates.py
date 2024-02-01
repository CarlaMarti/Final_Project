import pandas as pd

def deal_with_duplicates():
    df = pd.read_csv("Dataset.csv")
    duplicates = df.duplicated()
    print("Duplicated rows:", df[duplicates].count().sum())
    duplicates_clientnum = df['CLIENTNUM'].duplicated()
    print("Duplicated clientnum:", df[duplicates_clientnum].count().sum())
    df.to_csv("Dataset.csv", index=False)

if __name__ == "__main__":
    deal_with_duplicates()
