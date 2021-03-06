# Intro to Streamlit

## Streamlit
https://streamlit.io/

- Library open source, seperti halnya Flask dan Django untuk membuat web apps.
- Memudahkan pengguna untuk mengubah data script menjadi aplikasi berbasis web.
- Dapat mendeploy Machine Learning dan membuat visualisasi data.

## Instalasi
Untuk mempermudah pengerjaan projek, kamu perlu tahu bagaimana memanggil Python versi 3 melalui terminal / command prompt.
- Pada Windows umumnya adalah dengan perintah `python`.
	- Kamu bisa mengeceknya dengan `python --version`.
- Pada Mac atau Linux umumnya adalah dengan perintah `python3`.
	- Kamu bisa mengeceknya dengan `pyhton3 --version`.
**Penting** : selalu gunakan Python dan PIP versi 3 untuk lab ini.
.     
Saya sangat menyarankan untuk menggunakan Visual Studio Code (VSCode) untuk lab kali ini. Kamu bisa menginstallnya pada https://code.visualstudio.com/.  
Di dalam VSCode kamu bisa menjalankan terminal, caranya adalah dengan memilih opsi terminal, seperti pada gambar berikut.  
![](attachments/Pasted%20image%2020220719133405.png)  
.  

### FAQ
- Q: Pada Windows, mengapa `python --version` tidak bisa dipanggil pada terminal?  
- A: Yang pertama, kamu perlu memastikan bahwa Python sudah terinstall pada komputer kamu. Kemudian, pastikan python juga sudah masuk ke dalam environment variable. Kamu bisa menggunakan guide ini https://www.youtube.com/watch?v=4bUOrMj88Pc.

## Step 1: Memastikan Python dan Instalasi PIP
Untuk troubleshooting, cobalah pastikan Python serta pip sudah terinstall pada komputer.   
.  
`python --version` atau `python3 --version`  pastikan dari perintah ini menggunakan Python versi terbaru.
Apabila belum terinstall, silahkan install Python terlebih dahulu atau juga pastikan Python sudah berada pada environment variable.
.  
`pip --version` atau `pip3 --version` pastikan menggunakan pip yang terhubung dengan python3.  
Apabila belum terinstall, silahkan install pip dengan menggunakan perintah di bawah ini.

**Windows**
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py 

pip --version
```

**Mac**
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python3 get-pip.py

pip --version
```

**Linux (APT)**
```sh
sudo apt install python3-pip

pip3 --version
```
.  

Update pip dengan menggunakan perintah di bawah.
```python
python -m pip install --upgrade pip # Windows

# atau...

python3 -m pip install --upgrade pip # Mac atau Linux
```

## Step 2: Instalasi dan Aktivasi Virtual Environment
Buat sebuah folder dan install virtual environment di dalam folder tersebut.
```sh
pip install virtualenv

mkdir streamlit

cd streamlit

# buat virtual environment dengan nama stenv
python -m venv stenv
```

Aktivasi virtual environment pada **Windows**.
```sh
stenv\Scripts\activate.bat
```

Aktivasi virtual environment pada **Mac dan Linux**
```sh
source stenv/bin/activate
```

Apabila sudah berhasil, akan muncul (stenv) sebelum prompt pada terminal.  
![](attachments/Pasted%20image%2020220719134014.png)  

## Step 3: Instalasi Streamlit
Pastikan bahwa virtual environment sudah berjalan.  
.  
Kemudian install streamlit di dalamnya.
```sh
pip install streamlit
```
.  
Jika berhasil, kamu dapat menjalankan Streamlit dengan menggunakan perintah di bawah ini.
```sh
streamlit hello
```

## Step 4: Eksplorasi Streamlit
Kamu bisa masuk ke dalam halaman Streamlit melalui browser dan memasukkan alamat http://localhost:8501/ .
.  
Cobalah untuk eksplorasi secara mandiri. Kamu akan melihat gambar berikut.  
![](attachments/Pasted%20image%2020220719140948.png)  

## Step 5: Membuat Website Sendiri dengan Streamlit
Bukalah folder `streamlit` dengan menggunakan VSCode. Kemudian buatlah `st1.py` dan masukkan script di bawah ini.
```python
import streamlit as st

st.write("Hai, aku Ismail")
st.write("Seorang programmer Python")
```
.  
Jalankan Website tersebut dengan Streamlit melalui terminal.
```sh
streamlit run st1.py
```
.  
Sekarang coba ubah codenya menjadi berikut dan save.
```python
import streamlit as st

st.write("Hai, aku Ismail")
st.write("Seorang programmer Python")
st.write("Kelas K - Emang Kece")
```
.  
Kemudian lihat kembali ke browser. Kamu akan mendapatkan prompt berikut ini.  
![](attachments/Pasted%20image%2020220719152257.png)   
Pilihlah `Always rerun` agar Streamlit mengambil update pada source code secara otomatis.

## Step 6: Tugas Kamu
Buatlah perkenalan singkat diri Anda. Contoh: nama, alamat, motivasi mengikuti pelatihan ini dengan menggunakan `st.write()`.

## Step 7 (optional): Memahami Virtual Environment pada Python
Penggunaan Python pada Virtual Environment ini memiliki benefit:
- Kita bisa menciptakan environment yang berbeda untuk menjaga kompatibilitas dari aplikasi. Contohnya, kita bisa menjalankan virtual environment python 3.8 pada sistem dengan requirement Python 3.10.
- Menjaga environment Python pada komputer tetap stabil (terutama pada Linux).
.  
Mencoba deaktivasi virtual environment pada Python
```sh
deactivate
```
.  
Dengan menggunakan perintah `deactivate`, maka kita akan keluar dari virtual environment, sehingga kita saat ini berada di system environment. Secara default, kita akan berada di system environment ketika kita baru saja masuk ke terminal. Untuk masuk kembali ke dalam virtual environment dan menjalankan Streamlit, kita perlu memasukkan kembail perintah sebelumnya.  
.  
Aktivasi virtual environment pada **Windows**.
```sh
stenv\Scripts\activate.bat
```

Aktivasi virtual environment pada **Mac dan Linux**
```sh
source stenv/bin/activate
```

Apabila sudah berhasil, akan muncul (stenv) sebelum prompt pada terminal.  
![](attachments/Pasted%20image%2020220719134014.png)  

