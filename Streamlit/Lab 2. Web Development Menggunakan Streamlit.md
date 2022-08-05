# Web Development Menggunakan Streamlit
https://docs.streamlit.io/library/api-reference  

## Step 1: Text Element
https://docs.streamlit.io/library/api-reference/text  
.  
Teknik untuk Display text pada Streamlit. Ada Beberapa yang akan kita coba.
- `st.title()`
- `st.header()`
- `st.subheader()`
- `st.caption()`
- `st.text()`
- `st.markdown()`
.  
Pada kesempatan kali ini, kita akan membuat Curriculum Vitae (CV) sederhana. 
```python
import streamlit as st

st.title("Curriculum Vitae")

st.header("Identitas Diri")
st.text("""
Nama        : Name 
Email       : Email
Hobi        : Hobbies
""")

st.header("Soft Skill")
st.subheader("Social")
st.text("Leadership, Business Talk, Public Speaking")

st.subheader("Technical Skill")
st.text("Web Programming, Python, Cloud Computing, Excel, Cyber Security")

st.caption("ssst... otw sukses!")
```

Hasilnya:  
![](attachments/Pasted%20image%2020220719160652.png)  
## Step 2: Implementasi Kolom pada Streamlit
https://docs.streamlit.io/library/api-reference/layout/st.columns  
https://docs.streamlit.io/library/api-reference/data/st.metric  
.  
Coba kita ubah bagian dari social skill dengan menggunakan `st.column()` untuk menciptakan CV yang lebih interaktif. Kamu bisa cari gambar yang dibutuhkan pada link: https://fonts.google.com/icons?icon.query=person .
```python
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
```

Hasilnya:
![](attachments/Pasted%20image%2020220719165813.png)  
.  
Kemudian kita juga bisa menggunakan `st.metric()` untuk menciptakan skill level supaya lebih fun. 
```python
st.header("Technical Skill")

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Web Programming", "3/5")
col2.metric("Python", "5/5")
col3.metric("Cloud Computing", "2/5")
col4.metric("Excel", "3/5")
col5.metric("Cyber Security", "4/5")
```

Jadi, untuk full codenya sampai saat ini adalah:
```python
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
```

Hasilnya:  
![](attachments/Pasted%20image%2020220719173512.png)  

## Step 3: Pembuatan Transkrip Nilai dengan Pandas
https://docs.streamlit.io/library/api-reference/data/st.dataframe.  
.  
Data yang kamu baca dengan library Pandas dapat ditampilkan pada Streamlit.
```python
st.header("\n")
st.header("Transkrip")
Transkrip = pd.DataFrame({
    "Mata Kuliah": ["Pemrograman Dasar", "Algoritma dan Struktur Data", "Keamanan Informasi"],
    "Nilai": ["A", "B", "A"]
})

st.dataframe(Transkrip)
```

## Step 4: Membawa Audio dan Video  ke dalam Streamlit
Kamu bisa download video dan audio sampel di https://pixabay.com/.  
https://docs.streamlit.io/library/api-reference#Media-elements  
.  
Cara memasukkan audio pada Streamlit.  
```python
st.header("\n")
st.header("My Music")
st.audio("public/cool_music.mp3")
st.text("\nMusik Ku, Jiwa Ku")
```
.  
Cara memasukkan video pada Streamlit.
```python
st.header("\n")
st.header("My Video")
st.video("public/Surfing.mp4")
st.text("This is my quality")
```

## Step 5: Multipage Apps





