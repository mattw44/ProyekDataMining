import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Prediction")

st.title("Ayo Ukur Tingkat Stres Kalian")
st.write("Masukkan data-data yang diperlukan dalam kolom-kolom berikut")

st.cache_resource 
def load_model(path):
  model=joblib.load(path)
  return model

model = load_model('model/decision_tree_model.pkl')
