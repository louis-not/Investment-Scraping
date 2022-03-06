import pandas as pd


def transform(df,writer, sheet):
    """Function for transforming data and converting to excel"""
    df = pd.DataFrame(df[0])
    df.rename(columns={'Unnamed: 0':'Sektor'})
    df.to_excel(writer, sheet)

    # print(df)
    pass


