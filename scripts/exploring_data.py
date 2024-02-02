from exploratory_analysis.general import plot_general_distributions
from exploratory_analysis.categorical_eda import CatEDA
from exploratory_analysis.numerical_eda import numerical_histograms
def exploring(df_to_explore, pgd, ceda, neda):
    """
    Explore the dataset
    """
    if False == (pgd or ceda or neda):
        print("\n\n\nYou didn't select any exploration method.\n\n\n")
    if pgd:
        df_to_explore = plot_general_distributions(df_to_explore)
    if ceda:
        cat_eda = CatEDA()
        cat_eda.categorical_bars(df_to_explore)
    if neda:
        numerical_histograms(df_to_explore)
    if False == (neda and pgd and ceda):
        print("\n\n\nRemember that there are still things to explore!\n\n\n")
    
    return df_to_explore

