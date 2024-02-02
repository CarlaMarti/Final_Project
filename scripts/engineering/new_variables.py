def creating_variables(df_to_engineer):
    # Variable 1: Average Amount per Transaction = Avg_Trans_Amt
    df_to_engineer = df_to_engineer.assign(Avg_Trans_Amt=lambda x: round(x['Total_Trans_Amt'] / x['Total_Trans_Ct'], 2))
    
    # Variable 2: Average Utilization Ratio in Percentage = Avg_Utilization_Ratio_Percentage
    df_to_engineer = df_to_engineer.assign(Avg_Utilization_Ratio_Percentage=lambda x: (x['Avg_Utilization_Ratio']*100))
    
    print("\n\n\nNew variables:\n\n",df_to_engineer[['Total_Trans_Amt','Total_Trans_Ct','Avg_Trans_Amt', 'Avg_Utilization_Ratio','Avg_Utilization_Ratio_Percentage']].head())
    return df_to_engineer
