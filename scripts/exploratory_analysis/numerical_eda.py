import seaborn as sns
import matplotlib.pyplot as plt
import os


def numerical_histograms(df_to_explore):
    """
    Numerical EDA
    """
    palette = sns.color_palette("Blues")
    for col in df_to_explore.columns:
        if df_to_explore[col].dtype != "O" and col != "CLIENTNUM":
            plt.figure(figsize=(8, 6))
            df_to_explore[col].plot(kind="hist", color="skyblue")
            plt.title(col.upper())
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            plt.xticks(rotation=45)
            output_dir = "exploring_data/numerical_histograms"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f"{col}_histogram.png")
            plt.savefig(output_path)
            plt.close()
