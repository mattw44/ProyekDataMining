import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Prediction")

st.title("Ayo Ukur Tingkat Stres Kalian")
st.write("Masukkan data-data yang diperlukan dalam kolom-kolom berikut")

@st.cache_resource  # Tambahkan tanda @ untuk decorator
def load_model(path):
    model = joblib.load(path)
    return model

model = load_model('model/decision_tree_model.pkl')

shpd = st.number_input("Study_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)  # hapus tanda " setelah angka default
ehpd = st.number_input("Extracurricular_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
s2hpd = st.number_input("Sleep_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
s3hpd = st.number_input("Social_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
pahpd = st.number_input("Physical_Activity_Hours_Per_Day", min_value=0.0, max_value=10.0, value=2.0)
grades = st.number_input("Grades", min_value=0.0, max_value=13.0, value=2.0)

if st.button("Prediksi"):  # tambahkan tanda titik dua ':'
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
label_map = {0: "Low", 1: "Moderate", 2: "High"}
hasil = model.predict(input_data)
label_hasil = label_map[hasil[0]]
st.success(f"Hasil Prediksi: {label_hasil}")
