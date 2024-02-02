import seaborn as sns
import matplotlib.pyplot as plt
import os

class CatEDA:
    def categorical_bars(self, df_to_explore):
        palette = sns.color_palette('Oranges')
        for col in df_to_explore.columns:
            if df_to_explore[col].dtype == 'O':
                plt.figure(figsize=(8, 6))  # Optional size for the figure
                df_to_explore[col].value_counts().plot(kind='bar', color=palette)
                plt.title(col.upper())  # Title with column name in uppercase
                plt.xlabel(col)  # Label for x-axis
                plt.ylabel('Count')  # Label for y-axis
                plt.xticks(rotation=45)  # Optional rotation of x-axis labels
                output_dir = 'exploring_data/categorical_bars'
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, f"{col}_barplot.png")  # Unique filename for each plot
                plt.savefig(output_path)
                plt.close()  # Close the current figure
