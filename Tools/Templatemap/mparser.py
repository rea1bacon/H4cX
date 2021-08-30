import colorama
from termcolor import colored
import requests as req



class parser:
    colorama.init()
    def parse_arg(self,coo):
        try:
            string = coo
            array = coo.split(";")
            ret = {}
            for i in array:
                final = []
                for ite in range(0,len(i)):
                    if i[ite]=="=":
                        final.append(i[0:ite])
                        final.append(i[ite+1:])
                ret[final[0]]=final[1]
            return ret
        except Exception as e:
            print(colored(f"[-] Error while parsing cookies, please check : {e}","red"))
            exit()


    def test_url(self,url,method):
        try:
            if method == "post":
                r = req.post(url)
            else:
                r = req.get(url)
            return True
        except Exception as e:
            print(colored(f"[-] Error with url : {e}","red"))
            exit()


    def check_param(self,url,param,method):
        #return the url in the good format
        if method == "get":
            if '?' not in url or param not in url:
                return url+'?'
            elif param not in url:
                url = url + '&'
                return url
            else:
                ind = url.index('?')
                part = url[ind+1:]
                url = url[:ind]
                li = []
                listed = part.split('&')
                for i in listed:
                    for l in i:
                        if l == "=":
                            temp_index = i.index(l)
                            temp = i[:temp_index]
                    if param not in temp:
                        li.append(i)
                return url+'?'+'&'.join(li)+'&'
        else:
            return url
