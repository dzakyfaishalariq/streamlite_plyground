def main():
    import streamlit as st

    pg = st.navigation(
        [
            st.Page(
                "pages/halaman_siswa_mat.py",
                title="Halaman Untuk Siswa Matematika",
                icon="📚",
                default=True,
            ),
            st.Page(
                "pages/halaman_siswa_por.py",
                title="Halaman Untuk Siswa Portugis",
                icon="📖",
            ),
            st.Page(
                "pages/halaman_siswa_gabungan.py",
                title="Halaman Untuk Siswa Gabungan",
                icon="📝",
            ),
        ]
    )

    pg.run()


if __name__ == "__main__":
    main()
