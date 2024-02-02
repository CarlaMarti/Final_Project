"""
Encoding
"""
import pandas as pd


def encoding_categorical(df_to_engineer):
    """
    Encoding categorical
    """
    print("\n\n\nENCODING")

    # label_encoding

    df_to_engineer["!ATTRITION_FLAG!"] = (
        df_to_engineer["Attrition_Flag"].astype("category").cat.codes
    )

    print(
        "\n\n", df_to_engineer[["Attrition_Flag",
                                "!ATTRITION_FLAG!"]].sample(5), "\n\n"
    )

    # one_hot_encoding

    columns_to_encode = [
        "Gender",
        "Education_Level",
        "Marital_Status",
        "Income_Category",
        "Card_Category",
    ]

    print(
        "\nColumns to encode:\n",
        df_to_engineer[columns_to_encode].sample(3), "\n\n\n"
    )

    encoded_dfs = []

    for category in columns_to_encode:
        df_encoded = pd.get_dummies(df_to_engineer[category], prefix=category)
        df_encoded = df_encoded.apply(
            lambda x: x.map({True: 1, False: 0})
        )
        encoded_dfs.append(df_encoded)

    df_to_engineer = pd.concat([df_to_engineer] + encoded_dfs, axis=1)

    print("\n\nActual variables:\n\n", df_to_engineer.columns)

    return df_to_engineer
