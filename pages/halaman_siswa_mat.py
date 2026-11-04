from pathlib import Path

import pandas as pd
import streamlit as st

BASELINE = Path(__file__).resolve().parent.parent
path_math = BASELINE / "datasets" / "student-mat.csv"

def main():
    df_math = pd.read_csv(path_math, sep=";")

    # title halaman
    st.title("Halaman Untuk Siswa Matematika")
    st.dataframe(df_math, hide_index=True)
    st.markdown("## Keterangan")
    st.markdown(f"- Ukuran matriks siswa matematika {df_math.shape[0]} x {df_math.shape[1]}")
    
    
if __name__ == "__main__":
    main()