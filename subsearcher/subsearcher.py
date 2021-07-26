import sys
import requests as req
import time


#init all var
count=1
url =""
inter = 50
word="common.txt"

try:
	arg = sys.argv[1]
except IndexError:
	raise SystemExit(f"No argument. Minimum 1 for url.")


for i in range(len(sys.argv[1:])):
	if sys.argv[count]=="-u":
		if type(sys.argv[count+1])== str:
			url=sys.argv[count+1]
		else:
			print("Url must be a string."+sys.argv[count+1]+" is a "+type(sys.argv[count+1]))

	if sys.argv[count]=="-i":
		if type(sys.argv[count+1])== str:
			inter=int(sys.argv[count+1])
		else:
			print("Interval must be an int."+sys.argv[count+1]+" is a "+type(sys.argv[count+1]))

	if sys.argv[count]=="-w":
                if type(sys.argv[count+1])== str:
                        word=sys.argv[count+1]
	count+=1


def search(ur,i,w):
	print('Testing...')

	inte=i/100
	with open(w) as f:
		lines = f.readlines()
		
	httpverify = ur[0:4]

	if httpverify != "http":
		ur= "http://"+ ur
	u = ur

	for i in range(len(lines)):
		ext = lines[i].replace("\n","")
		nurl = u + ext
		resp = req.get(nurl)
		if resp.status_code != 404:
			print('[+]-One new url found :',nurl,'with response code ['+str(resp.status_code)+'] and SIZE :', len(resp.content))
		time.sleep(inte)


search(url , inter,word)

