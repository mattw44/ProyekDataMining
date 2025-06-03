import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Prediction")

st.title("Ayo Ukur Tingkat Stres Kalian")
st.write("Masukkan data-data yang diperlukan dalam kolom-kolom berikut")

#Memanggil model yang akan digunakan
@st.cache_resource 
def load_model(path):
    model = joblib.load(path)
    return model

model = load_model('model/decision_tree_model.pkl')

#Mendefinisikan variabel input
nama = st.text_input("Masukkan nama Anda:")
shpd = st.slider("Study_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)  # hapus tanda " setelah angka default
ehpd = st.slider("Extracurricular_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
s2hpd = st.slider("Sleep_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
s3hpd = st.slider("Social_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
pahpd = st.slider("Physical_Activity_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
grades = st.slider("Grades", min_value=0.0, max_value=10.0, value=2.0)

#Menampilkan hasil prediksi 
if st.button("Prediksi"):  
    input_data = pd.DataFrame(
        [[shpd, ehpd, s2hpd, s3hpd, pahpd, grades]],
        columns=[
            "Study_Hours_Per_Day",
            "Extracurricular_Hours_Per_Day",
            "Sleep_Hours_Per_Day",
            "Social_Hours_Per_Day",
            "Physical_Activity_Hours_Per_Day",
            "Grades"
        ]
    )
    hasil = model.predict(input_data)
    st.success(f"Halo Kak {nama}, tingkat stess kamu adalah {hasil[0]}")
    st.success(f"Semoga harimu menyenangkan")
