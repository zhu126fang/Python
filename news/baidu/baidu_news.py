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

f1=open('./baidu_news' + today + '.txt','w')

#pdb.set_trace()

post_url='http://news.baidu.com/' #Get the Data
print post_url
#f1.write(post_url + '\n')
try:
    rp = post(post_url)
    soup = BeautifulSoup(rp,"html.parser")

    hotnews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
    for li in hotnews:
	f1.write(li.a['href'].ljust(85))
	f1.write('|' + li.a.text.encode('utf-8'))
	f1.write('\n') 

    Aul = soup.find_all("ul",class_="ulist focuslistnews")
    print len(Aul)

    for ul in Aul:
	#ulparent = ul.parent
	#ulattrs = ulparent.findAll("div", attrs={"alog-group":True});
        #print ulattrs["alog-group"]

	Ali = ul.find_all("li")
	#pdb.set_trace()
        print len(Ali)
	for li in Ali:
	    #print li.a['href']
	    #print li.a.text
	    f1.write(li.a['href'].ljust(85))
	    f1.write('|' + li.a.text.encode('utf-8'))
	    f1.write('\n')    
except:
    print (today + "Error")    
f1.close
print ('Fin')
