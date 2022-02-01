# Intro Metasploit

## Shell Payload
Dieksekusi setelah eksploitasi berhasil, tujuannya adalah untuk mendapatkan akses ke komputer target. Anggap saja seperti mendapatkan terminal pada komputer target. 
Reverse shell

Bind Shell, why bind shell

Meterpreter

## Staged vs Non-staged
Non-staged: 
- Exploit shellcode dikirimkan langsung seluruhnya. 
- Size besar
- Tidak selalu berhasil
- windows/meterpreter_reverse_tcp

Staged:
- Payload dikirimkan berkala
- Terkadang kurang stabil
- Contoh: windows/meterpreter/reverse_tcp

