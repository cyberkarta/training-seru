import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.title("Curriculum Vitae")
    st.subheader("")


col1, col2 = st.columns(2)

with col1:
   st.image("images/profpic.png")

with col2:
    st.text("""
    .
    .
    .
    """)
    st.header("Identitas Diri")
    st.text("""
    Nama        : Name 
    Email       : Email
    Hobi        : Hobbies
    """)
    st.text("""
    .
    .
    .
    """)

st.header("\n")
st.header("Social Skill")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/leadership.png")
    st.subheader("Leadership")
    st.caption("Menghandle tim kecil untuk startup")

with col2:
    st.image("images/business.png")
    st.subheader("Business Talk")
    st.caption("Public Relation untuk startup")

with col3:
    st.image("images/presentation.png")
    st.subheader("Public Speaking")
    st.caption("Presentasi di depan klien")


st.header("\n")
st.header("Technical Skill")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Web Programming", "3/5")
col2.metric("Python", "5/5")
col3.metric("Cloud Computing", "2/5")
col4.metric("Excel", "3/5")
col5.metric("Cyber Security", "4/5")

st.header("\n")
st.header("Transkrip")
Transkrip = pd.DataFrame({
    "Mata Kuliah": ["Pemrograman Dasar", "Algoritma dan Struktur Data", "Keamanan Informasi"],
    "Nilai": ["A", "B", "A"]
})

st.dataframe(Transkrip)


st.header("\n")
st.header("My Music")
st.audio("public/cool_music.mp3")
st.text("\nMusik Ku, Jiwa Ku")


st.header("\n")
st.header("My Video")
st.video("public/Surfing.mp4")
st.text("This is my quality")


st.caption("ssst... otw sukses!")
