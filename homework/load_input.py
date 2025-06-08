import pandas as pd


import glob


def load_input(input_directory,input_number):
    files = glob.glob(f"{input_directory}/tbl{input_number}.tsv")
    dataframes = [
        pd.read_csv(
            file,
            delimiter="\t",
            index_col=None,
        )
        for file in files
    ]

    dataframe = pd.concat(dataframes, ignore_index=True)

    return dataframe