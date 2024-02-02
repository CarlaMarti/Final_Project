

def eliminar_nulos(df_to_clean):
    """
    Delete null values
    """
    print("Valores nulos antes: \n", df_to_clean.isnull().sum(), "\n\n\n")
    numeric_columns = df_to_clean.select_dtypes(include=["number"]).columns
    categorical_columns = df_to_clean.select_dtypes(exclude=["number"]).columns

    for column in numeric_columns:
        df_to_clean[column].fillna(df_to_clean[column].mean(), inplace=True)

    df_to_clean.dropna(subset=categorical_columns, inplace=True)

    print("Valores nulos despues: \n", df_to_clean.isnull().sum(), "\n")
    return df_to_clean
