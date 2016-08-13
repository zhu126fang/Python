#coding=gb18030
import pdb
import requests
import sys
import time
import urllib
import urllib2
import datetime
from urllib import urlencode
from bs4 import BeautifulSoup

def post(url):
    req = urllib2.Request(url)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req)
    return response.read()

today = datetime.date.today().strftime("%Y-%m-%d")
print today

f1=open('./huanqiu_world' + today + '.txt','w')

#pdb.set_trace()

post_url='http://world.huanqiu.com/article/' #Get the Data
print post_url
#f1.write(post_url + '\n')
try:
    rp = post(post_url)
    soup = BeautifulSoup(rp,"html.parser")

    Ali = soup.find_all("li",class_="item")
    print len(Ali)
    for i in range(0,len(Ali)):
	li = Ali[i]
	f1.write(li.h6.text.ljust(20))
	f1.write(li.a['href'].ljust(65))
	f1.write(li.a['title'].encode('utf-8'))
	f1.write('\n')
    for i in range(2,31):
	new_post_url = post_url + str(i) + '.html'
	print new_post_url
    	rp = post(new_post_url)
    	soup = BeautifulSoup(rp,"html.parser")

    	Ali = soup.find_all("li",class_="item")
    	print len(Ali)
	for i in range(0,len(Ali)):
	    li = Ali[i]
	    f1.write(li.h6.text.ljust(20))
	    f1.write(li.a['href'].ljust(65))
	    f1.write(li.a['title'].encode('utf-8'))
	    f1.write('\n') 
    	#pdb.set_trace()
except:
    print (today + "Error")    
f1.close
print ('Fin')
