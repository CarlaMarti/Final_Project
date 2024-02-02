

def repeated_values(df_to_clean):
    print("We see the different categories of gender repeated:")
    print(df_to_clean["Gender"].value_counts())

    df_to_clean["Gender"] = df_to_clean["Gender"].str.capitalize()

    print("\n\n\nAfter capitalization, now we only have male and female:")
    print(df_to_clean["Gender"].value_counts())
    return df_to_clean
