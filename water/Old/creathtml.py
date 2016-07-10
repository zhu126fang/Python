#!/usr/bin/python
import pdb
import urllib2
from bs4 import BeautifulSoup
import sys
import time

reload(sys)
sys.setdefaultencoding('gb18030')
datename = time.strftime('%Y%m%d_%H%M%S',time.localtime(time.time()))

url = 'http://www.ctg.com.cn/inc/sqsk.php?NeedCompleteTime2=2013-01-01'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, from_encoding = 'gb18030')

print soup

pdb.set_trace()
f1=open('./html/main' + datename + '.html','w')

f1.write('<!DOCTYPE html>' + '\n')
f1.write('<html>' + '\n')
f1.write('<head>' + '\n')
f1.write('<meta charset="gb18030">' + '\n')
f1.write('<meta http-equiv="X-UA-Compatible" content="chrome=1">' + '\n')
f1.write('<link href="http://www.5ichai.com/css/page318.css" rel="stylesheet">' + '\n')
f1.write('<link rel="shortcut icon" href="favicon.ico" />' + '\n')
f1.write('<title>news' + datename + '</title>' + '\n')
f1.write('</head>' + '\n')
f1.write('<body>' + '\n')

f1.write('<section class="ml_title">' + '\n')
f1.write('<h1>News</h1>' + '\n')
f1.write('<span>By Francis</span>' + '\n')
f1.write('</section>' + '\n')
f1.write('<section class="mlad"></section>' + '\n')
f1.write('<section class="ml_main">' + '\n')
f1.write('<dl>' + '\n')
f1.write('<dt>HOT NEWS</dt>' + '\n')

hotnews = soup.find_all('div', {'class', 'hotnews'})[0].find_all('li')
for i in hotnews:
	text = i.a.text
	href = i.a['href']
	f1.write('<dd><a href=' + href + '>' + text + '</a></dd>' + '\n')
focusnews = soup.find_all('ul',class_='ulist focuslistnews')

for i in focusnews:
	f1.write('<dt></dt>')
#	pdb.set_trace()
	ia = i.find_all('a')
	for j in ia:
		text = j.text
		href = j['href']
		f1.write('<dd><a href=' + href + '>' + text + '</a></dd>' + '\n')

f1.write('<section class="tixing">Attention</section>' + '\n')
f1.write('</body>' + '\n')
f1.write('</html>' + '\n')
f1.close
