import pandas as pd

def delete_last_two_columns():
    try:
        df = pd.read_csv("Dataset.csv")
        print("\n\nColumnas antes:\n",list(df.columns),"\n\n\n")
        df = df.iloc[:, :-2]
        df.to_csv("Dataset.csv", index=False)
        print("\n\nColumnas después:\n", list(df.columns))
        print("\n\nSe eliminaron las dos últimas columnas exitosamente.")
    except Exception as e:
        print("Ocurrió un error:", e)

if __name__ == "__main__":
    delete_last_two_columns()
