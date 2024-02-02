import pandas as pd


def deal_with_duplicates(df_to_clean):
    duplicates = df_to_clean.duplicated()
    print("Duplicated rows:", df_to_clean[duplicates].count().sum())
    df_to_clean.drop_duplicates(inplace=True)
    print("Updated duplicated rows:", df_to_clean[duplicates].count().sum())
    duplicates_clientnum = df_to_clean["CLIENTNUM"].duplicated()
    print("Duplicated clientnum:", df_to_clean[duplicates_clientnum].count().sum())
    df_to_clean.drop_duplicates("CLIENTNUM", inplace=True)
    print(
        "Updated duplicated clientnum:", df_to_clean[duplicates_clientnum].count().sum()
    )
    return df_to_clean
