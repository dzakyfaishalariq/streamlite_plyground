# import numpy as np
import pandas as pd


def merge_dataframes(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    """
    Merge two DataFrames on a specified column.

    Parameters:
    df1 (pd.DataFrame): The first DataFrame.
    df2 (pd.DataFrame): The second DataFrame.
    on (str): The column name to merge on.

    Returns:
    pd.DataFrame: The merged DataFrame.
    """
    marge_cols = [
        "school",
        "sex",
        "age",
        "address",
        "famsize",
        "Pstatus",
        "Medu",
        "Fedu",
        "Mjob",
        "Fjob",
        "reason",
        "nursery",
        "internet",
    ]

    merged_df = pd.merge(df1, df2, on=marge_cols, how='inner', suffixes=('_math', '_por'))
    return merged_df
