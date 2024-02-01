import click
import pandas as pd

@click.command(short_help='Parser to manage inputs for BooksDataset')#info
@click.option('-r','--read_data', is_flag=True, help='Read the dataset.')

def main(read_data):
    """
    Read the the dataset.
    """
    if read_data:
            
        print("\n\n\nYou will now read the dataset!\n\n\n")
        try:
            df = pd.read_csv("Dataset.csv", sep=',')
        except FileNotFoundError as e:
            raise FileNotFoundError(f"\n\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!CAUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n FILE COULDN'T BE FOUND: {e}\n\n\n\n")
        print(df)
        print("\n\n\nYou have read the dataset!\n\n\n")
    
    
if __name__ == '__main__':
    print("\n\n\nInstruction received!\n\n\n")
    main()