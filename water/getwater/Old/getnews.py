#!/usr/bin/python
#update 2016-3-17
#shield the link.txt

import pdb
import urllib2
from bs4 import BeautifulSoup
import sys
import time

#pdb.set_trace()
datename = time.strftime('%Y%m%d',time.localtime(time.time()))

reload(sys)
sys.setdefaultencoding('gb18030')
url = 'http://news.baidu.com/'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, from_encoding = 'gb18030')

f = open('./html/main' + datename + '.txt','w')
f1= open('./html/link' + datename + '.txt','w')
hotnews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotnews:
	#print i.a.text
	#print i.a['href']
	f.write(i.a.text + '\n')
	f.write(i.a['href'] + '\n')
	f1.write(i.a['href'] + '\n')
focusnews = soup.find_all('ul',class_='ulist focuslistnews')

for i in focusnews:
	#print "______________________________________________"
	f.write('\n')
	ia = i.find_all('a')
	for j in ia:
		#print j.text
		#print j['href']
		f.write(j.text + '\n')
		f.write(j['href'] + '\n')
		f1.write(j['href'] + '\n')
f.close
f1.close
