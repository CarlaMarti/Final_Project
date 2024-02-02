import numpy as np


def mistakendata(df_to_clean):
    print(
        "General description of the variable to have a general idea:\n\n\n",
        df_to_clean["Dependent_count"].describe(),
        "\n\n\n",
    )
    print(
        "Unique values that the variable takes:",
        df_to_clean["Dependent_count"].unique(),
    )
    if (df_to_clean["Dependent_count"] < 0).any():
        df_to_clean["Dependent_count"] = df_to_clean[
            "Dependent_count"].replace(
            -1, np.nan
        )
    print(
        "Unique values that the variable takes:",
        df_to_clean["Dependent_count"].unique(),
    )
    return df_to_clean
