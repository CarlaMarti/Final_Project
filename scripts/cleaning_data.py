import click
from cleaning.irrelevant import delete_last_two_columns
from cleaning.outliers import outliersfunction
from cleaning.mistaken import mistakendata
from cleaning.nulos import eliminar_nulos

@click.command()
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-ir', is_flag=True, help='Delete last 2 columns from the dataset')
@click.option('-md', is_flag=True, help='Delete mistaken data')
@click.option('-vn', is_flag=True, help='Delete null values')

def cleaning(ir, out, md, vn):
    if ir:
        delete_last_two_columns()
    if out:
        outliersfunction()
    if md:
        mistakendata()
    if vn:
        eliminar_nulos()
if __name__ == '__main__':
    cleaning()
