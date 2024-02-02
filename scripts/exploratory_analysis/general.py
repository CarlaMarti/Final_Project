import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_general_distributions(df_to_explore):
    fig, (
        (ax1, ax2, ax3, ax4),
        (ax5, ax6, ax7, ax8),
        (ax9, ax10, ax11, ax12),
        (ax13, ax14, ax15, ax16),
    ) = plt.subplots(nrows=4, ncols=4, figsize=(15, 15))

    plt.subplots_adjust(
        hspace=0.5, wspace=0.5
    )  # Ajuste de espaciado vertical y horizontal

    df_to_explore["Attrition_Flag"].value_counts().plot(kind="bar", ax=ax1)

    sns.boxplot(x=df_to_explore["Customer_Age"], ax=ax2)

    df_to_explore["Gender"].value_counts().plot(kind="bar", ax=ax3)

    sns.boxplot(x=df_to_explore["Dependent_count"], ax=ax4)

    df_to_explore["Education_Level"].value_counts().plot(kind="bar", ax=ax5)

    df_to_explore["Marital_Status"].value_counts().plot(kind="bar", ax=ax6)

    df_to_explore["Income_Category"].value_counts().plot(kind="bar", ax=ax7)

    df_to_explore["Card_Category"].value_counts().plot(kind="bar", ax=ax8)

    sns.boxplot(x=df_to_explore["Months_on_book"], ax=ax9)

    sns.boxplot(x=df_to_explore["Credit_Limit"], ax=ax10)

    sns.boxplot(x=df_to_explore["Total_Revolving_Bal"], ax=ax11)

    sns.boxplot(x=df_to_explore["Avg_Open_To_Buy"], ax=ax12)

    sns.boxplot(x=df_to_explore["Total_Amt_Chng_Q4_Q1"], ax=ax13)

    sns.boxplot(x=df_to_explore["Total_Trans_Amt"], ax=ax14)

    sns.boxplot(x=df_to_explore["Total_Trans_Ct"], ax=ax15)

    sns.boxplot(x=df_to_explore["Total_Ct_Chng_Q4_Q1"], ax=ax16)

    output_dir = "exploring_data/general"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "General_Distributions.png")
    plt.savefig(output_path)

    plt.close(fig)
