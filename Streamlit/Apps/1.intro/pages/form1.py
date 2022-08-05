import streamlit as st

st.title("Kenalan Yuk")

with st.form("kenalan"):
    st.write("Kenalan Yuk")
    nama = st.text_input("Nama Kamu: ")
    deskripsi = st.text_area("Deskripsi Diri: ")
    pekerjaan = st.selectbox("Pekerjaan", ["Siswa", "Mahasiswa", "Swasta", "Pegawai Negeri", "Dokter", "Guru"])
    minat_python = st.slider("Kamu Suka Python?", min_value=0, max_value=5, step=1, value=5)

    tombol_submit = st.form_submit_button("Submit")


if tombol_submit :
    st.write(f"Hai {nama} yang seorang {pekerjaan.lower()} salam kenal yak...")
    
    if minat_python <= 3 :
        st.write("Python itu nyenengin kok...")
    else:
        st.write("Suka Python? Samaan deh.")

# Opsi lain, bisa menggunakan object notation
# form = st.form(key='my_form')
# form.text_input(label='Enter some text')
# submit_button = form.form_submit_button(label='Submit')

st.title("Skill Kamu")
col1, col2 = st.columns(2)

with col1:
    with st.form("program"):
        st.selectbox("Bahasa Pemrograman Favorit", ["Python", "C++", "Pascal"])
        st.slider("Seberapa Pede Kamu?", min_value=0, max_value=5, step=1, value=5)
        submit_program = st.form_submit_button("Submit")
        if submit_program:
            st.write("Kamu sudah submit")

with col2:
    with st.form("olahraga"):
        st.selectbox("Olahraga Favorit", ["Jogging", "Sepedaan", "Renang"])
        st.slider("Seberapa Sering Kamu Olahraga?", min_value=0, max_value=5, step=1, value=5)
        submit_olahraga = st.form_submit_button("Submit")
        if submit_olahraga:
            st.write("Kamu sudah submit")


st.title("Rekomendasi Kuliner Kamu")

with st.form("kuliner"):
    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Rekomendasi 1: ")
    
    with col2:
        st.text_input("Rekomendasi 2: ")
    
    submit_kuliner = st.form_submit_button("Submit")

if submit_kuliner:
    st.write("Terimakasih rekomendasinya :smile:")


st.title("Pertanyaan Dikit")

with st.form("pertanyaan"):
    soal1 = st.radio(
        "Nasi terbuat dari apa?", 
        ["Beras", "Aspal", "Es Teh", "Biji kedelai pilihan"]
        )
    submit = st.form_submit_button("Submit")

    if submit:
        if soal1 == "Beras":
            st.write("Yak Benar...")
        else: 
            st.write("Ooops...")