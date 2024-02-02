def understandingdata(df):
    """
    A script to provide an overview of the dataset.
    """
    try:
        print("\n\n\nDataset Overview:\n\n\n\n")
        print(f"\n\n\nNumber of rows: {df.shape[0]}")
        print(f"\n\n\nNumber of columns: {df.shape[1]}")
        print("\n\n\n\nColumns and data types:")
        print(df.dtypes)
        print("\n\n\n\nColumn Names:")
        print(list(df.columns))
        print("\n\n\n\nDescription:")
        print(df.describe())
        print("\n\n\n\nUnique Values per Column:")
        for column in df.columns:
            print(f"{column}: {df[column].nunique()}")
        print("\n\n\n\nMissing Values per Column:")
        print(df.isnull().sum())
        print("\n\n\n\nExample of Unique Values per Column:")
        for column in df.columns:
            unique_values = df[column].unique()[:4]
            print(f"{column}: {unique_values}")
        print("\n\n\n\nSample of Data:")
        print(df[['CLIENTNUM', 'Attrition_Flag', 'Customer_Age', 'Gender', 'Income_Category']].sample(5))  # Mostrar las primeras filas como una tabla sin índices
    except FileNotFoundError:
        print("Dataset not found!")

