import numpy as np
import pandas as pd


def pencegahKebocoranData(df: pd.DataFrame, kolom_target: str) -> pd.DataFrame:
    """
    Fungsi untuk mencegah kebocoran data dengan menghapus kolom target dari DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame yang akan diproses.
    kolom_target (str): Nama kolom target yang akan dihapus.

    Returns:
    pd.DataFrame: DataFrame tanpa kolom target.
    """
    if kolom_target in df.columns:
        df = df.drop(columns=[kolom_target])
    return df


def rekayasaKolomTarget(df: pd.DataFrame, kolom_target: str):
    # target untuk regresi
    y_mat_regresi = df[kolom_target]
    # target untuk klasifikasi
    y_mat_klasifikasi = np.where(df[kolom_target] >= 10, 1, 0)

    return y_mat_regresi, y_mat_klasifikasi


def transformasiFiturKategorik(df: pd.DataFrame):
    binary_cols = [
        "schoolsup",
        "famsup",
        "paid",
        "activities",
        "nursery",
        "higher",
        "internet",
        "romantic",
    ]

    df[binary_cols] = df[binary_cols].replace({"yes": 1, "no": 0})
    # melakukan label encoding
    df["school"] = df["school"].map({"GP": 1, "MS": 0})
    df["sex"] = df["sex"].map({"F": 1, "M": 0})
    df["address"] = df["address"].map({"U": 1, "R": 0})
    df["famsize"] = df["famsize"].map({"LE3": 1, "GT3": 0})
    df["Pstatus"] = df["Pstatus"].map({"T": 1, "A": 0})

    # One hot encoding
    one_cols = ["Mjob", "Fjob", "reason", "guardian"]
    df = pd.get_dummies(df, columns=one_cols, dtype=int)
    return df


def transformasiFiturKategorikGanda(df: pd.DataFrame):
    binary_cols_merged = [
        "nursery",
        "internet",
        "schoolsup_mat",
        "schoolsup_por",
        "famsup_mat",
        "famsup_por",
        "paid_mat",
        "paid_por",
        "activities_mat",
        "activities_por",
        "higher_mat",
        "higher_por",
        "romantic_mat",
        "romantic_por",
    ]

    df[binary_cols_merged] = df[binary_cols_merged].replace({"yes": 1, "no": 0})

    df["school"] = df["school"].map({"GP": 1, "MS": 0})
    df["sex"] = df["sex"].map({"F": 1, "M": 0})
    df["address"] = df["address"].map({"U": 1, "R": 0})
    df["famsize"] = df["famsize"].map({"LE3": 1, "GT3": 0})
    df["Pstatus"] = df["Pstatus"].map({"T": 1, "A": 0})

    one_cols_merged = ["Mjob", "Fjob", "reason", "guardian_mat", "guardian_por"]
    df = pd.get_dummies(df, columns=one_cols_merged, dtype=int)
    return df
