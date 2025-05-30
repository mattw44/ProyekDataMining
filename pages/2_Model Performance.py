import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Model Performance")

st.title("Model Performa")
st.write("Pilih model performa yang kalian inginkan")

df = pd.read_csv("model/Data Student lifestyle.csv", sep=';')

testing = st.slider("Data Testing", min_value=10, max_value=90, value=20)
st.write(f"Nilai yang dipilih: {testing}")
t_size = testing/100

X = df.drop('Stress_Level', axis=1)
y = df['Stress_Level']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=t_size, random_state=42)

@st.cache_resource
def load_model(path):
    model = joblib.load(path)
    return model
