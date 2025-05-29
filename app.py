import streamlit as st
import pandas as pd

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Main Menu")

st.title("Selamat datang di aplikasi Pengukur Tingkat Stres Mahasiswa")
st.write("Aplikasi ini dibuat untuk mengukur tingkat stres mahasiswa berdasarkan gaya hidup.")

#Load Dataset
df = pd.read_csv("model/Data Student lifestyle.csv", sep=';')

# Menampilkan dataframe
st.subheader("📂 Data Gaya Hidup Mahasiswa")
st.dataframe(df, use_container_width=True)

st.subheader("📌 Jumlah Data Berdasarkan Tingkat Stres")
kelas_counts = df['Tingkat Stres'].value_counts()
for label, jumlah in kelas_counts.items():
st.write(f"- **{label}**: {jumlah} data")
st.table(kelas_counts.reset_index().rename(columns={'index': 'Tingkat Stres', 'Tingkat Stres': 'Jumlah'}))
