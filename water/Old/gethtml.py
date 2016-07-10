#!/usr/bin/python
#update 2016-3-18
#1. get the news
#2. use the date to creat the dir
#2. get the links html

import os
import urllib
import cookielib
from urlparse import *

import pdb
import urllib2
from bs4 import BeautifulSoup
import sys
import time

reload(sys)
sys.setdefaultencoding('gb18030')

cj = cookielib.LWPCookieJar()
opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

datename = time.strftime('%Y%m%d',time.localtime(time.time()))
try:
	os.makedirs('./html/'+ datename)
except:
	print 'make dir Err!'

url = 'http://news.baidu.com/'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, from_encoding = 'gb18030')

#test input 'N' to next
#pdb.set_trace()

#Get the host news
hotnews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotnews:
	title = i.a.text
	link  = i.a['href']
	#print link
	req = urllib2.Request(link)
        try:
                operate = opener.open(req)
                msg = operate.read()
		
                linkparse = urlparse(link)
		filename = './html/' + datename + '/' + linkparse.netloc + '.html'
		filename = './html/' + datename + '/' + title + '.html'

		#print filename
		flink = open(filename,'w')
                flink.write(msg)
                flink.close
        except:
                #print "404 Err"
		filename = './html/' + datename + '/' +  '404 Err ' + title + '.html'
		flink = open(filename,'w')
                flink.write(link)
                flink.close

#Get the focuslistnews		
focusnews = soup.find_all('ul',class_='ulist focuslistnews')
for i in focusnews:
	ia = i.find_all('a')
	for j in ia:
		title = j.text
		link  = j['href']
		#print link
		req = urllib2.Request(link)
        	try:
                	operate = opener.open(req)
                	msg = operate.read()
		
                	linkparse = urlparse(link)
			filename = './html/' + datename + '/' + linkparse.netloc + '.html'
			filename = './html/' + datename + '/' + title + '.html'

			#print filename
			flink = open(filename,'w')
                	flink.write(msg)
                	flink.close
        	except:
                	#print "404 Err"
					filename = './html/' + datename + '/' + '404 Err '  + title + '.html'
					#flink = open(filename,'w')
                	#flink.write(link)
                	#flink.close
