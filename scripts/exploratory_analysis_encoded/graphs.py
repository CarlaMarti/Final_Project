import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Verifica si la carpeta "graphs" existe, si no, la crea
if not os.path.exists("graphs"):
    os.makedirs("graphs")


def guardar_grafico(fig, nombre):
    ruta = os.path.join("graphs", nombre + ".png")
    fig.savefig(ruta)
    print(f"Grafico guardado como: {ruta}")


def visualize_variables(df):
    # Gráfico 1
    fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(
        nrows=3, ncols=2, figsize=(15, 15)
    )
    fig.suptitle(
        "CTD MONETARIA EN TRANSACCIONES Y NUM DE TRANSACCIONES",
        fontsize=20
    )

    sns.boxplot(data=df, x="Total_Trans_Amt", y="Attrition_Flag", ax=ax1)
    sns.boxplot(data=df, x="Total_Trans_Ct", y="Attrition_Flag", ax=ax2)

    sns.histplot(
        data=df, x="Total_Trans_Amt", hue="Attrition_Flag",
        ax=ax3, multiple="stack"
    )
    sns.histplot(
        data=df, x="Total_Trans_Ct", hue="Attrition_Flag",
        ax=ax4, multiple="stack"
    )

    heatmap_ = pd.crosstab(df["Attrition_Flag"], df["Total_Trans_Amt"])
    row_perc = heatmap_.div(heatmap_.sum(axis=1), axis=0) * 100
    sns.heatmap(row_perc, annot=True, fmt=".1f",
                cmap="Blues", linewidths=0, ax=ax5)
    ax5.set_title("Heatmap Total_Trans_Amt")

    heatmap_ = pd.crosstab(df["Attrition_Flag"], df["Total_Trans_Ct"])
    row_perc = heatmap_.div(heatmap_.sum(axis=1), axis=0) * 100
    sns.heatmap(row_perc, annot=True, fmt=".1f",
                cmap="Blues", linewidths=0, ax=ax6)
    ax6.set_title("Heatmap Total_Trans_Ct")

    guardar_grafico(fig, "grafico_1")

    # Gráfico 2
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(
        nrows=2, ncols=2, figsize=(15, 15))
    fig.suptitle("NUMERO DE PRODUCTOS (TOTAL RELATIONSHIP COUNT)",
                 fontsize=20)

    sns.boxplot(data=df, x="Total_Relationship_Count",
                y="Attrition_Flag", ax=ax1)
    ax1.set_xlabel("Number of products")
    ax1.set_title("Number of bank products contracted")
    ax1.set_ylabel("")

    counts = df.groupby(["Total_Relationship_Count", "Attrition_Flag"]
                        ).size().unstack()
    counts.plot(kind="bar", stacked=True, ax=ax2)
    ax2.set_xlabel("Number of products")
    ax2.set_title("Number of bank products contracted")
    ax2.set_ylabel("Count of clients")

    counts = df.groupby(["Total_Relationship_Count",
                        "Attrition_Flag"]).size().unstack()
    percentages = counts.div(counts.sum(axis=1), axis=0) * 100
    attrited_customer = percentages.loc[:, "Attrited Customer"]
    existing_customer = percentages.loc[:, "Existing Customer"]

    ax3.bar(
        attrited_customer.index, attrited_customer.values,
        label="Attrited Customer"
    )
    for i, v in enumerate(attrited_customer.values):
        ax3.text(i + 1, v, f"{round(v, 2)}", ha="center", va="center")
    ax3.set_xlabel("Number of products")
    ax3.set_ylabel("% of each category")
    ax3.set_title("Num of bank products contracted - Attrited")
    ax3.legend()

    ax4.bar(
        existing_customer.index, existing_customer.values,
        label="Existing Customer"
    )
    for i, v in enumerate(existing_customer.values):
        ax4.text(i + 1, v, f"{round(v, 2)}", ha="center", va="center")
    ax4.set_xlabel("Number of products")
    ax4.set_ylabel("% of each category")
    ax4.set_title("Num of bank products contracted - Existing")
    ax4.legend()

    guardar_grafico(fig, "grafico_2")

    # Gráfico 3
    fig, ((ax1,
           ax2), (ax3, ax4)) = plt.subplots(nrows=2,
                                            ncols=2, figsize=(15, 15))
    fig.suptitle("Num MESES INACTIVOS ÚLTIMO AÑO", fontsize=20)

    sns.boxplot(data=df, x="Months_Inactive_12_mon",
                y="Attrition_Flag", ax=ax1)
    ax1.set_xlabel("Number of months")
    ax1.set_title("Months inactive in the last year")
    ax1.set_ylabel("")

    counts = df.groupby(["Months_Inactive_12_mon",
                        "Attrition_Flag"]).size().unstack()
    counts.plot(kind="bar", stacked=True, ax=ax2)
    ax2.set_xlabel("Number of months")
    ax2.set_title("Months inactive in the last year")
    ax2.set_ylabel("Count of clients")

    counts = df.groupby(["Months_Inactive_12_mon",
                        "Attrition_Flag"]).size().unstack()
    percentages = counts.div(counts.sum(axis=1), axis=0) * 100
    attrited_customer = percentages.loc[:, "Attrited Customer"]
    existing_customer = percentages.loc[:, "Existing Customer"]

    ax3.bar(
        attrited_customer.index, attrited_customer.values,
        label="Attrited Customer"
    )
    for i, v in enumerate(attrited_customer.values):
        ax3.text(i, v, f"{round(v, 2)}", ha="center", va="center")
    ax3.set_xlabel("Number of months")
    ax3.set_ylabel("Percentage of clients")
    ax3.set_title("Months inactive in the last year - Attrited Customer")
    ax3.legend()

    ax4.bar(
        existing_customer.index, existing_customer.values,
        label="Existing Customer"
    )
    for i, v in enumerate(existing_customer.values):
        ax4.text(i, v, f"{round(v, 2)}", ha="center", va="center")
    ax4.set_xlabel("Number of months")
    ax4.set_ylabel("Percentage of clients")
    ax4.set_title("Months inactive in the last year - Existing Customer")
    ax4.legend()

    guardar_grafico(fig, "grafico_3")

    print("Graficos hechos!")
