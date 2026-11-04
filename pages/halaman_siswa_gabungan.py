from pathlib import Path

import pandas as pd
import streamlit as st

from tool.fungsi_marge import merge_dataframes

Basedir = Path(__file__).resolve().parent.parent
Filepath_math = Basedir / "datasets" / "student-mat.csv"
Filepath_por = Basedir / "datasets" / "student-por.csv"

# load data
df1 = pd.read_csv(Filepath_math, sep=";")
df2 = pd.read_csv(Filepath_por, sep=";")

# marge dataframes
df_marged = merge_dataframes(df1, df2)

st.title("Halaman Untuk Siswa Gabungan")
# membuat colom colom untuk menampilkan data
# data siswa matematika
col1, col2 = st.columns(2)

with col1:
    st.subheader("Data Siswa Matematika")
    st.dataframe(df1, hide_index=True)
with col2:
    st.subheader("Data Siswa Portugis")
    st.dataframe(df2, hide_index=True)

st.markdown("## Keterangan")
st.markdown("- Kolom pada data siswa matematika")
badges_math = " ".join([f':green-badge[{item}]' for item in df1.columns.to_list()])
st.markdown(badges_math)
st.markdown("- Kolom pada data siswa portugis")
badges_por = " ".join([f":green-badge[{item}]" for item in df2.columns.to_list()])
st.markdown(badges_por)

st.markdown("---")
st.markdown("## Data Siswa Gabungan")
st.dataframe(df_marged, hide_index=True)
st.markdown(f"Jumlah Data Siswa Gabungan: {len(df_marged)}")
