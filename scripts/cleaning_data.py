import click
from cleaning.outliers import outliersfunction
from cleaning.outliers import outliersfunction
from cleaning.outliers import outliersfunction
from cleaning.outliers import outliersfunction
from cleaning.outliers import outliersfunction


@click.command()
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')
@click.option('-out', is_flag=True, help='Detect and remove outliers from dataset')

def cleaning(ir, out):
    if ir:
        outliersfunction()
    elif out:
        outliersfunction()
    else:
        print("No action taken. Please use '-out' flag to detect and remove outliers.")

if __name__ == '__main__':
    cleaning()
