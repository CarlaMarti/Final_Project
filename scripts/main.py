import click
from read_data import read
from understanding import understandingdata
from cleaning_data import cleaning


@click.command(short_help='Parser to manage inputs for BooksDataset')
@click.option('-d','--dataset', required = True, help='Read the dataset.')
@click.option('-u', '--understanding', is_flag=True, help='Understand the data.')
@click.option('-c', '--datacleaning', is_flag=True, help='Clean the data.')
@click.option('-ir', '--remove_irrelevant_columns', is_flag=True, help='Delete last 2 columns from the dataset')
@click.option('-out', '--remove_outliers', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-md', '--remove_mistaken_data', is_flag=True, help='Delete mistaken data')
@click.option('-vn', '--remove_null_values', is_flag=True, help='Delete null values')
@click.option('-rep', '--remove_repeated', is_flag=True, help='Delete repeated values')
@click.option('-dup', '--remove_duplicates', is_flag=True, help='Delete duplicated values or users')


def main(dataset, understanding, datacleaning, remove_irrelevant_columns, remove_outliers, remove_mistaken_data, remove_null_values, remove_repeated, remove_duplicates):
    """
    Main code.
    """
    df = read(dataset)
    
    if understanding:
        understandingdata(df)

    if datacleaning:
        df_to_clean = df.copy()
        cleaning(df_to_clean, remove_irrelevant_columns, remove_outliers, remove_mistaken_data, remove_null_values, remove_repeated, remove_duplicates)

    
if __name__ == '__main__':
    print("\n\n\nInstruction received!\n\n\n")
    main()