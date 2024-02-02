"""
Read data
"""
import pandas as pd


def read(dataset):
    """
    Read the the dataset.
    """
    print("\n\n\nYou will now read the dataset!\n\n\n")
    try:
        df = pd.read_csv(dataset, sep=",")
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"\n\nFILE COULDN'T BE FOUND: {e}\n\n"
        )
    print(df)
    print("\n\n\nYou have read the dataset!\n\n\n")
    return df
