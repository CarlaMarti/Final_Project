from engineering.new_variables import creating_variables
from engineering.encoding import encoding_categorical


def feature_engineering_(df_to_engineer, nvar, enc):
    """
    Explore the dataset
    """
    if False == (nvar or enc):
        print("\n\n\nYou didn't select any engineering method.\n\n\n")
    if nvar:
        df_to_engineer = creating_variables(df_to_engineer)
    if enc:
        df_to_engineer = encoding_categorical(df_to_engineer)
    if False == (nvar and enc):
        print("\n\n\nRemember that there are still things to engineer!\n\n\n")

    return df_to_engineer
