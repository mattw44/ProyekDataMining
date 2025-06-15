import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Main Menu")

#Memberikan Judul dan Gambar yang menarik
st.title("APLIKASI MENGUKUR TINGKAT STRES")
st.write("Aplikasi ini dibuat untuk mengukur tingkat stres mahasiswa berdasarkan gaya hidup.")
st.image ("https://dinkes.bandaacehkota.go.id/wp-content/uploads/sites/36/2025/02/stress.png")

st.markdown("""
🧠 **Deskripsi Aplikasi**

Aplikasi ini dirancang untuk mengukur dan memprediksi tingkat stres mahasiswa berdasarkan gaya hidup mereka. 
Terdapat tiga menu utama dalam aplikasi ini:

1. 📊 **Dashboard**  
   Menampilkan data gaya hidup mahasiswa, statistik deskriptif, serta visualisasi grafik batang dan pie chart.

2. 📈 **Model Performance**  
   Menyediakan evaluasi performa model machine learning, seperti akurasi dan confusion matrix.

3. 🤖 **Prediksi**  
   Menggunakan model machine learning untuk memprediksi tingkat stres mahasiswa berdasarkan input gaya hidup.

""")

st.write ("Oleh Kelompok 16")
