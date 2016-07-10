#!/usr/bin/python
import urllib
import urllib2
import cookielib

from urlparse import *
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

datename = time.strftime('%Y%m%d',time.localtime(time.time()))

cj = cookielib.LWPCookieJar()
opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

f=open('./html/link' + datename + '.txt',"r")
links=f.readlines()

f.close

for link in links:
	print link
	req = urllib2.Request(link)
	try:
		operate = opener.open(req)
		msg = operate.read()

		linkparse=urlparse(link)
		links[links.index(link)] = linkparse.netloc
	
		flink=open('./html/' + datename + '/' + linkparse.netloc + '.html',"w")
		flink.write(msg)
		flink.close
	except:
		print "Err"
