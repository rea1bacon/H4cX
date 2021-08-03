# Cookies

## JWT token

### None algo 

Jwt cookies can be vulnerable if signature is not properly checked !
If so, we can modify the alg to none and delete the signature and modify the payload.

### Weak secret

We can crack the signature too with jwt tool https://github.com/ticarpi/jwt_tool

### RS256 to HS256

Misconfigured backend can be vunlerable if it doesnt check properly the return algo.
If we modify the algo from RS256 to HS256 and we use the public key as the secret, the backend will check the token with HS256 algo with the public key as the signature

HOW TO 

Save the key in a key.pem file
	❗❗❗ Respect this format
	-----BEGIN PUBLIC KEY-----
	key
	-----END PUBLIC KEY----- 

		import jwt
		public = open('key.pem','r').read()
		public = "\n".join(public.split('\n'))+"\n"
		print(jwt.encode({"username":"admin"}, key=public, algorithm='HS256')) 


