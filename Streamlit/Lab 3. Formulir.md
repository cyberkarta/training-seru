# Formulir
Membuat formulir pada Streamlit dapat dilakukan dengan menggunakan perintah `st.form`. Berikut ini adalah list perintah yang akan digunakan:
- `st.text_input`
- `st.text_area`
- `st.selectbox`
- `st.slider`
- `st.radio`
- `st.form_submit_button`

## Step 1: Dasar dari Formulir
Ada dua syntax untuk menotasikan pembuatan formulir pada streamlit, yaitu dengan menggunakan `with` atau dengan menggunakan notasi object.  
.
Dengan menggunakan `with`:
```python
with st.form("formulirku"):
	submit = st.form_submit_button("Submit")
```
.  
Dengan menggunakan notasi object:
```python
formulirku = st.form("formulirku")
submit = formulirku.form_submit_button("Submit")
```
.  
Untuk kemudahan dari praktikum ini, kita akan menggunakan versi pertama dengan definisi form menggunakan `with`.  
.  
Apabila formulir sudah dibuat, terdapat syarat untuk memasukkan submit button. Apabila submit button tidak dibuat, maka akan muncul pesan error.  Fungsi submit button ini sepertihalnya `st.button`, perbedaannya adalah `st.form_submit_button` berisi boolean yang mengindikasikan apakah formulir tersebut telah disubmit atau belum.

## Step 2: Membuat Formulir Polling untuk User
Untuk memulai membuat formulir, kita perlu definisikan formulir ini dengan langkah yang sudah dijelaskan pada step 1.
```python
import streamlit as st

st.title("Kenalan Yuk")

with st.form("kenalan"):
	st.write("Kenalan Yuk")
	
	tombol_submit = st.form_submit_button("Submit")
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805113956.png)  
.  
## Step 3: Mengambil Input dari User
Sekarang kita edit isi dari formulir kenalan dengan menampilkan formulir .  
```python
with st.form("kenalan"):
    st.write("Kenalan Yuk")
    nama = st.text_input("Nama Kamu: ")
    deskripsi = st.text_area("Deskripsi Diri: ")
    
    tombol_submit = st.form_submit_button("Submit")
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805114741.png)  
.  

## Step 4: Menambahkan Drop Down Menu
Tambahkan `st.selectbox` untuk menampilkan dropdown menu kepada user. Dropdown value pada `st.selectbox` didefinisikan dengan menggunakan tipe data list.  
```python
with st.form("kenalan"):
    st.write("Kenalan Yuk")
    nama = st.text_input("Nama Kamu: ")
    deskripsi = st.text_area("Deskripsi Diri: ")
    pekerjaan = st.selectbox("Pekerjaan", ["Siswa", "Mahasiswa", "Swasta", "Pegawai Negeri", "Dokter", "Guru"])

	tombol_submit = st.form_submit_button("Submit")
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805115238.png)  

## Step 5: Menambahkan Slider
Sekarang, kamu bisa menambahkan slider dengan perintah `st.slider`. Slider ini bisa diatur `min_value`, `max_value`, `step`, dan `value` (default value yang tertampil), sehingga kita diberi fleksibilitas dalam pengambilan data dari user.  
```python
with st.form("kenalan"):
    st.write("Kenalan Yuk")
    nama = st.text_input("Nama Kamu: ")
    deskripsi = st.text_area("Deskripsi Diri: ")
    pekerjaan = st.selectbox("Pekerjaan", ["Siswa", "Mahasiswa", "Swasta", "Pegawai Negeri", "Dokter", "Guru"])
    minat_python = st.slider("Kamu Suka Python?", min_value=0, max_value=5, step=1, value=5)

    tombol_submit = st.form_submit_button("Submit")
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805120018.png)  

## Step 6: Mengambil Informasi dari Isian Formulir
Untuk mengambil informasi dari formulir, kamu hanya perlu memanggil variabelnya saja. Contoh ketika ingin mengambil dan menampilkan informasi nama dan pekerjaan.
```python
st.write(f"Hai {nama} yang seorang {pekerjaan.lower()} salam kenal yak...")
```
.  
Bagian menariknya adalah kita dapat mengolah informasi yang telah dimasukkan oleh user.
```python
if minat_python <= 3 :
        st.write("Python itu nyenengin kok...")
    else:
        st.write("Suka Python? Samaan deh.")
```
.  
Sayangnya, pada step ini informasi pengolah data sudah dijalankan walaupun belum ada data user yang dimasukkan. Untuk menghindari layanan "awkward" ini, kita bisa melakukan checking ke boolean yang dihasilkan oleh method `st.form_submit_button()`.
```python
if tombol_submit :
    st.write(f"Hai {nama} yang seorang {pekerjaan.lower()} salam kenal yak...")
    
    if minat_python <= 3 :
        st.write("Python itu nyenengin kok...")
    else:
        st.write("Suka Python? Samaan deh.")
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805121118.png)  

## Step 7: Penggunaan Kolom
Sekarang, kita mencoba melihat interaksi penggunaan kolom terhadap formulir yang dibuat.  
.  
Pembuatan formulir di dalam kolom.  
```python
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
```
.  
Pembuatan kolom di dalam formulir.  
```python
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
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805122322.png)  
.  
Apakah teman-teman bisa melihat perbedaannya?

## Step 7: Membuat Quiz Sederhana dengan Radio Button
Kita juga bisa menggunakan radio button dengan perintah `st.radio` untuk melakukan polling kepada user.
```python
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
```
.  
Hasilnya adalah:  
![](attachments/Pasted%20image%2020220805124136.png)  

## Hasil Akhir Code
```python
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
```
.  
Hasil akhir:  
![](attachments/Pasted%20image%2020220805124606.png)  

.  

  

