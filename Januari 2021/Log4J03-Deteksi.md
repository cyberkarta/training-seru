# Percobaan Deteksi Log4J

## Uji Deteksi Pada Windows Defender
Windows Defender merupakan antivirus bawaan pada Windows. Uji deteksi ini menggambarkan kemampuan Windows Defender untuk mendeteksi file eksploitasi Log4j.

- Buka URL, copy isi dari file tersebut ke dalam notepad https://raw.githubusercontent.com/cyberkarta/weha/main/WebHacking/DES5-Log4J.md.
- Tunggu hingga Windows Defender bereaksi.

## Uji Deteksi pada Traffic Di Network
Uji deteksi ini menggambarkan kemampuan deteksi Log4j pada Next Gen Firewall, Intrusion Detection System, dan Intrusion Prevention System. 

- Install Snort
```sh
sudo apt install snort
```

- Buat rule di snort
```sh
sudo nano /etc/snort/rules/local.rules

# tambahkan di bagian paling bawah
alert tcp any any -> any any (msg: "Deteksi Log4Shell"; content: "${jndi:ldap://"; sid:202144228)
```
- Download pcap pada folder pcap
```
wget 
```
- Deteksi dari pcap
```sh
sudo snort -c /etc/snort/snort.conf -A console -r no_encrypt.pcap -l ./logs -k none 
```

Apakah terdeteksi?


## Uji Deteksi pada Traffic Terenkripsi di Network
Uji deteksi ini menggambarkan kemampuan deteksi Log4j pada Next Gen Firewall, Intrusion Detection System, dan Intrusion Prevention System. 


## Saran untuk Defender/Ops/Developer
https://github.com/NCSC-NL/log4shell/tree/main/software




