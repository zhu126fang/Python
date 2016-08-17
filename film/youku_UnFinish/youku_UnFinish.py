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

f1=open('./youku' + today + '.txt','w')

post_url='http://list.youku.com/category/video/c_0.html' #Get the Data
#post_url='http://list.youku.com/category/show/c_97.html' #Get the Data
print post_url
try:
    rp = post(post_url)
    soup = BeautifulSoup(rp,"html.parser")
    #pdb.set_trace()
    Adiv = soup.find_all("div",class_="yk-col4")
    print len(Adiv)
    for div in Adiv:
	Ali = div.find_all('li')

	print Ali[0].text
	print Ali[2].text
	print Ali[1].a['href']
	print Ali[1].a.text
	f1.write(Ali[0].text.ljust(10))
	f1.write(Ali[2].text.encode('utf-8').ljust(20))
	f1.write(Ali[1].a['href'].ljust(60))
	f1.write(Ali[1].a.text.encode('utf-8'))
	f1.write('\n')
    pdb.set_trace()

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
