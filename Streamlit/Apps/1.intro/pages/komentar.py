import streamlit as st
import sqlite3


conn = sqlite3.connect("komentar.db")
c = conn.cursor()

st.title("Masukkan Komentar Kalian")

with st.form("komentar", clear_on_submit=True):
    input_nama = st.text_input("Nama")
    input_judul = st.text_input("Judul Komentar")
    input_komentar = st.text_area("Komentar Kamu")
    submit_komentar = st.form_submit_button("Submit")

st.title("10 Komentar Terakhir")

if submit_komentar:
    c.execute("INSERT INTO komentar VALUES (:nama, :judul, :komentar)", { "nama": input_nama, "judul": input_judul, "komentar": input_komentar })

    conn.commit()

c.execute("SELECT * FROM komentar")
data = c.fetchmany(10)

for i in data:
    st.write(f"**{i[1]}** dari {i[0]}")
    st.write(i[2])
    st.write("\n")


