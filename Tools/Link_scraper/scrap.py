# This script can be really improved and is not otpimized for performance (python doesn't help)
import requests
import argparse
import re 
from bs4 import BeautifulSoup

# parsing args
parser = argparse.ArgumentParser()
parser.add_argument('-u', type=str, dest='url', required=True, help='Url of the target')
parser.add_argument('-r', type=int, dest='rec', default=1, help='Recursion of scraping')
args = parser.parse_args()


# class for every single link
# struct : url of the link
#		   all the link on the page
class lin:
	def __init__(self,url: str,sub: list):
		self.sub = sub
		self.url = url



# class for the scraper
class scr:
	#attribute of the scraper
	def __init__(self,url,maxr):
		#root url
		self.url = url
		#the list of links
		self.table = []
		#init recursion
		self.rec = 0
		#set max recursion
		self.max = maxr


	# scraping function
	# will add the links to the table by creating new class lin each time	
	def scrap(self,t,p):
		f  = [x for x in map(self.deldo,t) if x is not None]
		self.table.append(lin(p,f))
		self.rec +=1
		# check if max recurion is reached 
		if self.rec < self.max :
			for i in f:
				if type(self.listlink(self.resp(i),i)) == "<class 'list'>":
					print(i)
					self.run(i)
			
		

	# return the link without href attr and give a good format
	def getlink(self, x):
		a = x[6:-1]
		if a[0:4] == "http":
			return a
		else:
			return args.url + a


	# function to list all the link with a simple regex
	# Then execute the function scrap with a list of all links
	def listlink(self, t,p):
		n = []
		a = re.findall('href="[\S]+"',t)
		n = list(map(self.getlink,a))
		self.scrap(n,p)


	# make a simple request to the link and get the content
	def resp(self, u):
		req = requests.get(u)
		return req.text


	# function to run the scraper
	def run(self,u):
		self.listlink(self.resp(u),u)

	
	# delete links with #, or duplicates links
	def deldo(self,o):
		if '#' not in o and self.url != o and self.url != o+"/" :
			return o



x = scr(args.url,args.rec)
x.run(args.url)
for i,a in enumerate(x.table, start=0):
	print(f'{a.url}\n{"-"*20}\n{a.sub}\n\n')