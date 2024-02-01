import click
from cleaning.irrelevant import delete_last_two_columns
from cleaning.outliers import outliersfunction
from cleaning.mistaken import mistakendata
from cleaning.nulos import eliminar_nulos
from cleaning.repeated import repeated_values
from cleaning.duplicates import deal_with_duplicates

@click.command()
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-ir', is_flag=True, help='Delete last 2 columns from the dataset')
@click.option('-md', is_flag=True, help='Delete mistaken data')
@click.option('-vn', is_flag=True, help='Delete null values')
@click.option('-rep', is_flag=True, help='Delete repeated values')
@click.option('-dup', is_flag=True, help='Delete duplicated values or users')

def cleaning(ir, out, md, vn, rep, dup):
    if ir:
        delete_last_two_columns()
    if out:
        outliersfunction()
    if md:
        mistakendata()
    if vn:
        eliminar_nulos()
    if rep:
        repeated_values()
    if dup:
        deal_with_duplicates()

if __name__ == '__main__':
    cleaning()
