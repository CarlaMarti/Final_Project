def delete_last_two_columns(df_to_clean):
    """
    Deletes the two irrelevant columns
    """
    try:
        print("\n\nColumnas antes:\n", list(df_to_clean.columns), "\n\n\n")

        if len(df_to_clean.columns) >= 2:
            df_to_clean = df_to_clean.iloc[:, :-2]
            print("\n\nColumnas después:\n", list(df_to_clean.columns))
            print("\n\nSe eliminaron las dos últimas columnas.\n\n")
        else:
            print("\n\nNo hay suficientes columnas para eliminar.\n\n")
    except Exception as e:
        print("Ocurrió un error:", e)
    return df_to_clean
