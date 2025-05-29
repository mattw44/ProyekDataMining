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

st.write(df.columns.tolist())
kelas_counts = df['Stress_Level'].value_counts()
