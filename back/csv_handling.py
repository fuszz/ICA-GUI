import pandas as pd


def csv_import(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename, sep=';')
    df = df.reset_index(drop=True)
    return df


def csv_export(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, sep=';')
