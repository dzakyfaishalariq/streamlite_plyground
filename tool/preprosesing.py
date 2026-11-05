import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def pencegahKebocoranData(df: pd.DataFrame, kolom_target: list) -> pd.DataFrame:
    """
    Fungsi untuk mencegah kebocoran data dengan menghapus kolom target dari DataFrame.

    Parameters:
    df (pd.DataFrame): DataFrame yang akan diproses.
    kolom_target (str): Nama kolom target yang akan dihapus.

    Returns:
    pd.DataFrame: DataFrame tanpa kolom target.
    """
    if isinstance(kolom_target, list):
        if all(k in df.columns for k in kolom_target):
            df = df.drop(columns=kolom_target)
    else:
        if kolom_target in df.columns:
            df = df.drop(columns=kolom_target)
    return df


def rekayasaKolomTarget(df: pd.DataFrame, kolom_target: str):
    # target untuk regresi
    y_regresi = df[kolom_target]
    # target untuk klasifikasi
    y_klasifikasi = pd.Series(
        np.where(df[kolom_target] >= 10, 1, 0),
        index=df.index,
        name="Target_klasifikasi",
    )

    return y_regresi, y_klasifikasi


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


def trainTestSplitTunggal(df, y_klasifikasi, y_regresi):
    X = df.drop(columns=["G1", "G2", "G3"])
    y_k = y_klasifikasi
    y_regg = y_regresi
    # digunakan untuk klasifikasi
    X_train_k, y_train_k, X_test_k, y_test_k = train_test_split(
        X, y_k, test_size=0.20, random_state=42, stratify=y_k
    )
    # digunakan untuk regresi
    X_train_r, y_train_r, X_test_r, y_test_r = train_test_split(
        X,
        y_regg,
        test_size=0.2,
        random_state=42,
    )

    data_klasifikasi = (X_train_k, y_train_k, X_test_k, y_test_k)
    data_regressi = (X_train_r, y_train_r, X_test_r, y_test_r)

    return data_klasifikasi, data_regressi


def trainTestSplitMajemuk(df, y_klasifikasi, y_regresi):
    X = df.drop(columns=["G1_mat", "G2_mat", "G3_mat", "G1_por", "G2_por", "G3_por"])
    y_k = y_klasifikasi
    y_regg = y_regresi
    # digunakan untuk klasifikasi
    X_train_k, y_train_k, X_test_k, y_test_k = train_test_split(
        X, y_k, test_size=0.20, random_state=42, stratify=y_k
    )
    # digunakan untuk regresi
    X_train_r, y_train_r, X_test_r, y_test_r = train_test_split(
        X,
        y_regg,
        test_size=0.2,
        random_state=42,
    )

    data_klasifikasi = (X_train_k, y_train_k, X_test_k, y_test_k)
    data_regressi = (X_train_r, y_train_r, X_test_r, y_test_r)

    return data_klasifikasi, data_regressi


def featureScalingTunggal(X_train, X_test):

    scaler = StandardScaler()
    X_train["absences"] = scaler.fit_transform(X_train[["absences"]])
    X_test["absences"] = scaler.transform(X_test["absences"])

    return X_train, X_test


def featurtScalingGanda(X_train, X_test):
    kolom_skala = ["absences_mat", "absences_pro"]
    scaler_marge = StandardScaler()
    X_train[kolom_skala] = scaler_marge.fit_transform(X_train[kolom_skala])
    X_test[kolom_skala] = scaler_marge.transform(X_test[kolom_skala])
    return X_train, X_test
