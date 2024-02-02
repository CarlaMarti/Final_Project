import os
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlations(df_to_explore_encoded):
    # Lista 1: Información del cliente y sus cuentas
    lista1 = [
        "CLIENTNUM",
        "Customer_Age",
        "Dependent_count",
        "Months_on_book",
        "Total_Relationship_Count",
        "Months_Inactive_12_mon",
        "Contacts_Count_12_mon",
        "Credit_Limit",
        "Total_Revolving_Bal",
        "Avg_Open_To_Buy",
        "!ATTRITION_FLAG!",
    ]

    # Lista 2: Actividad financiera y transaccional
    lista2 = [
        "Total_Amt_Chng_Q4_Q1",
        "Total_Trans_Amt",
        "Total_Trans_Ct",
        "Total_Ct_Chng_Q4_Q1",
        "Avg_Utilization_Ratio",
        "Avg_Trans_Amt",
        "Avg_Utilization_Ratio_Percentage",
        "!ATTRITION_FLAG!",
    ]

    # Lista 3: Información demográfica y de cuenta
    lista3 = [
        "Gender_F",
        "Gender_M",
        "Education_Level_College",
        "Education_Level_Doctorate",
        "Education_Level_Graduate",
        "Education_Level_High School",
        "Education_Level_Post-Graduate",
        "Education_Level_Uneducated",
        "Education_Level_Unknown",
        "Marital_Status_Divorced",
        "Marital_Status_Married",
        "Marital_Status_Single",
        "Marital_Status_Unknown",
        "Income_Category_$120K +",
        "Income_Category_$40K - $60K",
        "Income_Category_$60K - $80K",
        "Income_Category_$80K - $120K",
        "Income_Category_Less than $40K",
        "Income_Category_Unknown",
        "Card_Category_Blue",
        "Card_Category_Gold",
        "Card_Category_Platinum",
        "Card_Category_Silver",
        "!ATTRITION_FLAG!",
    ]

    # Acercamiento 1: características sociales del cliente
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_to_explore_encoded[lista1].corr(), cmap="Blues", annot=True)
    if not os.path.exists("correlations"):
        os.makedirs("correlations")
    plt.savefig("correlations/correlation1.png")

    # Acercamiento 2: actividad financiera
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_to_explore_encoded[lista2].corr(),
                cmap="Greens", annot=True)
    plt.savefig("correlations/correlation2.png")

    # Acercamiento 3: información demográfica y de cuenta
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_to_explore_encoded[lista3].corr(), cmap="Reds", annot=True)
    plt.savefig("correlations/correlation3.png")

    print("\n\nImages have been saved!\n\n")
