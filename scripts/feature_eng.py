from engineering.new_variables import creating_variables

def feature_engineering_(df_to_engineer, nvar):
    """
    Explore the dataset
    """
    if False == (nvar):
        print("\n\n\nYou didn't select any engineering method.\n\n\n")
    if nvar:
        df_to_engineer = creating_variables(df_to_engineer)
    if False == (nvar):
        print("\n\n\nRemember that there are still things to engineer!\n\n\n")
    
    return df_to_engineer

