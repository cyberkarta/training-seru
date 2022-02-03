# Memakai Metasploit 2
## Modul
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

