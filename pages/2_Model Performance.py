import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

st.set_page_config(page_title="Aplikasi Tingkat Stres", layout="centered")
st.sidebar.header("Model Performance")

st.title("Model Performa")
st.write("Pilih model performa yang kalian inginkan")

#Memanggil model yang akan digunakan
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

model = load_model('model/decision_tree_model.pkl')

#Menampilkan Hasil Performa
if st.button("Hasil"):
    try:
        # Prediksi
        y_pred = model.predict(X_test)

        # Evaluasi
        accuracy = accuracy_score(y_test, y_pred) * 100
        precision = precision_score(y_test, y_pred, average='weighted') * 100
        recall = recall_score(y_test, y_pred, average='weighted') * 100
        f1 = f1_score(y_test, y_pred, average='weighted') * 100

        # Classification report
        report = classification_report(y_test, y_pred, output_dict=True)
        report_df = pd.DataFrame(report).transpose()

        # Tampilan hasil
        st.success("✅ Hasil Evaluasi Decision Tree Classifier")
        a, b = st.columns(2)
        c, d = st.columns(2)
        a.metric("🎯 Akurasi", f"{accuracy:.1f}%", border=True)
        b.metric("📏 Presisi", f"{precision:.1f}%", border=True)
        c.metric("📡 Recall", f"{recall:.1f}%", border=True)
        d.metric("📊 F1-Score", f"{f1:.1f}%", border=True)

        with st.expander("🔍 Lihat Classification Report Lengkap"):
            st.dataframe(report_df)

    except Exception as e:
        st.error(f"Terjadi kesalahan saat evaluasi model: {e}")
