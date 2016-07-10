#!/usr/bin/python
from urlparse import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
f=open('link.txt',"r")
links=f.readlines()
f.close

for link in links:
	#print link
	linkparse=urlparse(link)
	links[links.index(link)] = linkparse.netloc

links2=list(set(links))
links2.sort()
for link in links2:
	print links2.index(link)
	print link
	
