import streamlit as st

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Main Menu")

st.title("Selamat datang pada di aplikasi Pengukur Tingkat Stres Mahasiswa")
st.write("Aplikasi ini dibuat untuk mengukur tingkat stres mahasiswa berdasarkan gaya hidup.")

#Load Dataset
df=pd.read_csv("model/Data Student lifestyle.csv")

#Tampilan Data Frame
st.subheader("Dataset Tingkat Stres Mahasiswa")
st.dataframe(df)
