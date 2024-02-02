from exploratory_analysis_encoded.correlations import plot_correlations
from exploratory_analysis_encoded.graphs import visualize_variables


def exploring_encoded(df_to_explore_encoded, corr, g):
    """
    Explore the dataset
    """
    if False == (corr or g):
        print("\n\n\nYou didn't select any exploration method.\n\n\n")
    if corr:
        df_to_explore_encoded = plot_correlations(df_to_explore_encoded)
    if g:
        df_to_explore_encoded = visualize_variables(df_to_explore_encoded)
    if False == (corr and g):
        print("\n\n\nRemember that there are still things to explore!\n\n\n")

    return df_to_explore_encoded
