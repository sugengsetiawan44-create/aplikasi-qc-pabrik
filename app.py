import streamlit as st
import joblib

model_tersimpan = joblib.load('model_qc_pabrik.pkl')

st.title("Sistem Pengecekan Kualitas Sampel Lab QC")
st.write("Masukkan data hasil pengukuran sensor/alat lab:")

suhu = st.number_input("Input Suhu Reaktor / Ruang (°C)", value=25.0)
ph = st.number_input("Input Nilai pH Sampel", value=7.0)

if st.button("Cek Kualitas"):
    hasil = model_tersimpan.predict([[suhu, ph]])[0]
    if hasil == 1:
        st.success("✅ LULUS QC (Parameter Sesuai Standar)")
    else:
        st.error("❌ GAGAL QC / ANOMALI (Periksa Ulang Proses!)")