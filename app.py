import streamlit as st
import pandas as pd

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Main Menu")

st.title("Selamat datang pada di aplikasi Pengukur Tingkat Stres Mahasiswa")
st.write("Aplikasi ini dibuat untuk mengukur tingkat stres mahasiswa berdasarkan gaya hidup.")

#Load Dataset
df=pd.read_csv("model/Data Student lifestyle.csv")

#Tampilan Data Frame
st.subheader("Dataset Tingkat Stres Mahasiswa")
st.dataframe(df)

st.writer(df.columns.tolist())
#df[target] = data target
#df['label'] = df['Stress_Level'].map({0:'High', 1:'Moderate', 2:'Low'})
class_counts = df['Stress_Level'].value_counts()
