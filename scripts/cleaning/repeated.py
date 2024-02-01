import pandas as pd

def repeated_values():
    df = pd.read_csv("Dataset.csv")
    print("We see the different categories of gender ( male and female are repeated ):")
    print(df['Gender'].value_counts())

    df['Gender'] = df['Gender'].str.capitalize()

    print("\n\n\nAfter capitalization, now we only have male and female:")
    print(df['Gender'].value_counts())
    df.to_csv("Dataset.csv", index=False)

if __name__ == "__main__":
    repeated_values()
