import streamlit as st
import pandas as pd

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Dashboard")

st.title("Selamat datang di aplikasi Pengukur Tingkat Stres Mahasiswa")
st.write("Aplikasi ini dibuat untuk mengukur tingkat stres mahasiswa berdasarkan gaya hidup.")

#Load Dataset
df = pd.read_csv("model/Data Student lifestyle.csv", sep=';')

# Menampilkan dataframe
st.subheader("📂 Data Gaya Hidup Mahasiswa")
st.dataframe(df, use_container_width=True)

st.write(df.columns.tolist())
kelas_counts = df['Stress_Level'].value_counts()

st.subheader("📊 Grafik Batang")
fig, ax = plt.subplots()
kelas_counts.plot(kind='bar', color=['skyblue', 'orange', 'lightgreen'], ax=ax)
ax.set_xlabel("Tingkat Stres")
ax.set_ylabel("Jumlah")
ax.set_title("Distribusi Tingkat Stres Mahasiswa")
st.pyplot(fig)

st.subheader("📈 Grafik Lingkaran (Pie Chart)")
fig, ax = plt.subplots()
colors = ['#66b3ff', '#ffcc99', '#99ff99']  # warna untuk tiap kelas
ax.pie(
    kelas_counts,
    labels=kelas_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    textprops={'fontsize': 12}
)
ax.axis('equal')  # memastikan bentuk lingkaran
st.pyplot(fig)
