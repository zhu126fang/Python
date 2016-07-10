#!/usr/bin/python
import pdb
import urllib2
from bs4 import BeautifulSoup
import sys
import time

reload(sys)
sys.setdefaultencoding('gb18030')
datename = time.strftime('%Y%m%d',time.localtime(time.time()))

url = 'http://news.baidu.com/'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, from_encoding = 'gb18030')

f1=open('./html/main' + datename + '.html','w')

f1.write('<!DOCTYPE html>' + '\n')
f1.write('<html>' + '\n')
f1.write('<head>' + '\n')
f1.write('<meta charset="gb18030">' + '\n')
f1.write('<meta http-equiv="X-UA-Compatible" content="chrome=1">' + '\n')
f1.write('<link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css" media="screen">' + '\n')
f1.write('<link rel="stylesheet" type="text/css" href="stylesheets/github-dark.css" media="screen">' + '\n')
#f1.write('<link rel="stylesheet" type="text/css" href="stylesheets/print.css" media="print">' + '\n')
f1.write('<link rel="shortcut icon" href="favicon.ico" />' + '\n')
f1.write('<title>news' + datename + '</title>' + '\n')
f1.write('</head>' + '\n')
f1.write('<body>' + '\n')
f1.write('<div class="container">' + '\n')

#pdb.set_trace()
hotnews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotnews:
	text = i.a.text
	href = i.a['href']
	f1.write('<li><a href=' + href + '>' + text + '</a></li>' + '\n')
focusnews = soup.find_all('ul',class_='ulist focuslistnews')

for i in focusnews:
	#print "______________________________________________"
	f1.write('<li></li>')
	ia = i.find_all('a')
	for j in ia:
		text = j.text
		href = j['href']
		f1.write('<li><a href=' + href + '>' + text + '</a></li>' + '\n')

f1.write('</div>' + '\n')
f1.write('</body>' + '\n')
f1.write('</html>' + '\n')
f1.close
