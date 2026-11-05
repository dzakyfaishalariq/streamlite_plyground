from pathlib import Path

import pandas as pd
import streamlit as st

from tool.preprosesing import *

BASELINE = Path(__file__).resolve().parent.parent
path_math = BASELINE / "datasets" / "student-mat.csv"


def main():
    df_math = pd.read_csv(path_math, sep=";")

    # title halaman
    st.title("Halaman Untuk Siswa Matematika")
    st.dataframe(df_math.head(), hide_index=True)
    st.markdown("## Keterangan")
    st.markdown(
        f"Ukuran matriks siswa matematika {df_math.shape[0]} x {df_math.shape[1]}"
    )
    st.markdown("---")
    st.markdown("## Normalisasi Data")
    # normalisasi data
    df_mat = pencegahKebocoranData(df_math, ["G1", "G2"])
    st.markdown("### Tahap 1 Pencegah kebocoran data")
    st.dataframe(df_mat.head())
    st.markdown("Menghapus kolom G1 dan G2")
    # Mengambil data target nya baik menggunakan regresi dan klasifikasi
    y_regresi, y_klasifikasi = rekayasaKolomTarget(df_mat, "G3")
    st.markdown("### Memisahkan data untuk regresi dan klasifikasi")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Target untuk regresi")
        st.dataframe(y_regresi.head())
        st.caption(f"type data : {y_regresi.dtype}")
    with col2:
        st.subheader("Target untuk klasifikasi")
        st.dataframe(y_klasifikasi.head())
        st.caption(f"type data : {y_klasifikasi.dtype}")
        st.caption("data target dibuat kondisi dengna nilai >= 10 maka 1 kalo tidak 0")


if __name__ == "__main__":
    main()
