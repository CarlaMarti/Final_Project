import click
from read_data import read
from understanding import understandingdata
from cleaning_data import cleaning
from exploring_data import exploring
from feature_eng import feature_engineering_
from exploring_data_encoded import exploring_encoded


@click.command(short_help="Parser to manage inputs for BooksDataset.")
@click.option("-d", "--dataset", required=True, help="Read the dataset.")
@click.option("-u", "--understanding", is_flag=True, help="Understand.")
@click.option("-c", "--datacleaning", is_flag=True, help="Clean the data.")
@click.option(
    "-ir",
    "--remove_irrelevant_columns",
    is_flag=True,
    help="Delete last 2 columns from the dataset",
)
@click.option(
    "-out",
    "--remove_outliers",
    is_flag=True,
    help="Detect and remove outliers from dataset",
)
@click.option(
    "-md", "--remove_mistaken_data", is_flag=True, help="Delete mistaken data"
)
@click.option("-vn", "--remove_null_values", is_flag=True, help="Delete null")
@click.option("-rep", "--remove_repeated", is_flag=True,
              help="Delete repeated")
@click.option(
    "-dup",
    "--remove_duplicates",
    is_flag=True,
    help="Delete duplicated values or users",
)
@click.option("-e", "--exploratory_a", is_flag=True, help="Explore dataset")
@click.option(
    "-pgd",
    "--plot_general_distributions",
    is_flag=True,
    help="Plot general distributions.",
)
@click.option("-ceda", "--categorical_eda", is_flag=True, help="Categ. EDA")
@click.option("-neda", "--numerical_eda", is_flag=True, help="Numerical EDA")
@click.option("-fe", "--feature_engineering", is_flag=True,
              help="Feature engineering.")
@click.option("-nvar", "--new_variables",
              is_flag=True, help="Create new variables.")
@click.option("-enc", "--encoding",
              is_flag=True, help="Encode categorical variables.")
@click.option(
    "-ee",
    "--exploratory_analysis_once_encoded",
    is_flag=True,
    help="Explore dataset with the feature engineering.",
)
@click.option("-corr", "--correlations", is_flag=True,
              help="See the relations between variables.")
@click.option("-g", "--graphs", is_flag=True,
              help="Graph the relationships with Attrition Flag.")
def main(
    dataset,
    understanding,
    datacleaning,
    remove_irrelevant_columns,
    remove_outliers,
    remove_mistaken_data,
    remove_null_values,
    remove_repeated,
    remove_duplicates,
    exploratory_a,
    plot_general_distributions,
    categorical_eda,
    numerical_eda,
    feature_engineering,
    new_variables,
    encoding,
    exploratory_analysis_once_encoded,
    correlations,
    graphs,
):
    """
    Main code.
    """
    df = read(dataset)

    if understanding:
        understandingdata(df)

    if datacleaning:
        df_to_clean = df.copy()
        cleaning(
            df_to_clean,
            remove_irrelevant_columns,
            remove_outliers,
            remove_mistaken_data,
            remove_null_values,
            remove_repeated,
            remove_duplicates,
        )

    if exploratory_a:
        df_to_explore = cleaning(df, True, True, True, True, True, True)
        exploring(
            df_to_explore, plot_general_distributions,
            categorical_eda, numerical_eda
        )

    if feature_engineering:
        df_to_engineer = cleaning(df, True, True, True, True, True, True)
        feature_engineering_(df_to_engineer, new_variables, encoding)

    if exploratory_analysis_once_encoded:
        df_to_engineer = cleaning(df, True, True, True, True, True, True)
        df_to_explore_encoded = feature_engineering_(
            df_to_engineer, True, True)
        exploring_encoded(df_to_explore_encoded, correlations, graphs)


if __name__ == "__main__":
    print("\n\n\nInstruction received!\n\n\n")
    main()
