
# Log4j
https://github.com/apache/logging-log4j2

## Intro
CVE-2021-44228 - Skor CVSS 10/10 (critical), vulnerability ini dinamakan Log4shell
https://nvd.nist.gov/vuln/detail/CVE-2021-44228
https://www.cvedetails.com/cve/CVE-2021-44228/

Tipe vulnerability: Insecure deserialization (deserialisasi yang tidak aman)
https://cwe.mitre.org/data/definitions/502.html

Versi yang terdampak: 2.2.0-beta9 s/d 2.12.1 serta 2.13.0 s/d 2.15.0
Pada versi 2.16.0 fungsi yang rentan sudah dihilangkan.

Platform bug bounty hunting bergejolak, hampir 1.700 laporan diterima oleh HackerOne dan bounty sebesar $249.500, atau sekitar 3.5 Milyar Rupiah dikeluarkan oleh perusahaan yang terimbas.

## Dampak dari Log4shell
Perusahaan besar juga terdampak: https://github.com/cisagov/log4j-affected-db/blob/develop/SOFTWARE-LIST.md. List ini juga dapat digunakan untuk mengamankan server milikmu, terutama apabila ada kontrak/kerjasama dengan perusahaan pada list tersebut.

Remote Code Execution (RCE): Hacker dapat mengeksekusi code pada server.

Yang mengeksploitasi sebagian besar sudah bukan manusia lagi, melainkan robot.

Malware yang menggunakan teknik eksploitasi ini:
Linux/Miner-ABU,Linux/Miner-ADH
Linux/Swrort-G (“Mettle”)
Troj/Ransom-GME (TellYouThePass ransomware)
Troj/StealthL-A (Stealth Loader)
App/StlthLdr-A (Stealth Loader installer, PUA)
Mal/ExpJava-AL, Mal/ExpJava-AN, Mal/ExpJava-AO (Khonsari downloaders)
Troj/JavaDl-AAN and Troj/Java-AIN (Khonsari downloaders)
Troj/JavaDl-AAO (N0t4n3xplo1t.class)
Troj/Mdrop-JMR, Troj/Mdrop-JMS, Troj/Mdrop-JMP
Troj/Khonsari-A (new)
Troj/JavaDl-AAN
Troj/Java-AIN
Troj/BatDl-GR
Mal/JavaKC-B
XMRig Miner (PUA)
Troj/Bckdr-RYB
Troj/PSDl-LR
Mal/ShellDl-A
Linux/DDoS-DT, Linux/DDoS-DS
Linux/Miner-ADG, Linux/Miner-ZS, Linux/Miner-WU
Linux/Rootkt-M


## Benefit Mengetahui Log4shell
Banyak vulnerability serupa
- Shellshock (2014)
- Java SQL Database (2022) -> cara eksploitasi persis sama dengan Log4shell

Bagi offensive security: membuka peluang untuk mendeteksi dan melaporkan vulnerability serupa.

Bagi defender: mengetahui tingkat keamanan dari sistem yang dibangun, pada kasus ini pada aplikasi berbasis Java.

Bagi DFIR: memperjelas jejak pencarian teknik serangan, terutama pada aplikasi berbasis Java.

Bagi developer: mengetahui versi aman dari Log4j.


## Versi Log4j Ter-aman Saat Ini
**Java 8**: 2.17.1

**Java 7**: 2.12.4

**Java 6**: 2.3.2



## Tambahan
CVE-2021-4428 bukan vulnerability terakhir pada Log4j
https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-37215/Apache-Log4j.html

DoS pada versi 2.16.0

## Resource
**Official Apache**
https://logging.apache.org/log4j/2.x/security.html

**Scanner:**
Burp Suite Professional
[https://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f](https://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f)

Vulnerability Scanner
https://github.com/CERTCC/CVE-2021-44228_scanner


**Berita:**
https://portswigger.net/daily-swig/log4j

https://news.sophos.com/en-us/2021/12/20/logjam-log4j-exploit-attempts-continue-in-globally-distributed-scans-attacks/

**Resource lainnya:**
https://github.com/cisagov/log4j-affected-db
