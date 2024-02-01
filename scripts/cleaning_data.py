import click
from cleaning.irrelevant import delete_last_two_columns
from cleaning.outliers import outliersfunction

@click.command()
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-ir', is_flag=True, help='Delete last 2 columns from the dataset')

def cleaning(ir, out):
    if ir:
        delete_last_two_columns()
    elif out:
        outliersfunction()
    else:
        print("Please, select an action")

if __name__ == '__main__':
    cleaning()
