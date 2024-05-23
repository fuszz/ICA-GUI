import pandas as pd


def csv_import(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def csv_export(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, sep=';')
