from exploratory_analysis.numerical_variables import plot_numerical_variables
from exploratory_analysis.general import plot_general_distributions
from exploratory_analysis.categorical_eda import categorical_bars

def exploring(df_to_explore, pgd, ceda, pnv):
    if False == (pnv or pgd):
        print("\n\n\nYou didn't select any exploration method.\n\n\n")
    if pgd:
        df_to_explore = plot_general_distributions(df_to_explore)
    if ceda:
        categorical_bars(df_to_explore)
    if pnv:
        df_to_explore = plot_numerical_variables(df_to_explore)

    if False == (pnv and pgd):
        print("\n\n\nRemember that there are still things to explore!\n\n\n")
    

    return df_to_explore

