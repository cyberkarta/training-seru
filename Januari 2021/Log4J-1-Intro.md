
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


## Benefit Mengetahui Log4shell
Banyak vulnerability serupa
- Shellshock (2014)
- Java SQL Database (2022) -> cara eksploitasi persis sama dengan Log4shell

Bagi offensive security: membuka peluang untuk mendeteksi dan melaporkan vulnerability serupa.

Bagi defender: mengetahui tingkat keamanan dari sistem yang dibangun, pada kasus ini pada aplikasi berbasis Java.

Bagi dfir: mempermudah pencarian jejak serangan pada aplikasi berbasis java


## Tambahan
CVE-2021-4428 bukan vulnerability terakhir pada Log4j
https://www.cvedetails.com/vulnerability-list/vendor_id-45/product_id-37215/Apache-Log4j.html

## Resource

**Scanner:**
Burp Suite Professional
[https://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f](https://portswigger.net/bappstore/b011be53649346dd87276bca41ce8e8f)

