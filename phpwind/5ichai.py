#coding=gb18030
#UTF-8 BOM
import pdb
import requests
import sys
import time
from bs4 import BeautifulSoup

import datetime

f1=open('./5ichai.html','w')
begin = datetime.date(2016,7,12)
end = datetime.date(2016,6,1)
d = begin
delta = datetime.timedelta(days=1)
while d >= end:
    datename=d.strftime("%Y-%m-%d")
    nian=d.strftime("%Y")
    yue=d.strftime("%m")
    ri=d.strftime("%d")
    print datename
    d -= delta

    post_url='http://www.5ichai.com/phpwind/' #Get the Data
    print post_url
    try:
        rp=requests.post(post_url)
        ##It is very important!
        rp.encoding='gb18030'
        soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
        Atr3 = soup.find_all('tr', {'class', 'tr3'})
        #f1.write(datename + '\t')
        for i in range(0,len(Atr3)):
            tr3=Atr3[i]
            print tr3.a.text
            post_url = post_url + tr3.a.get('href')
            print (post_url)

            ###Main Pages
            rp=requests.post(post_url)
            ##It is very important!
            rp.encoding='gb18030'
            soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
            pages = soup.find_all('div', {'class', 'pages'})
            Aa = pages[0].find_all('a')
            for i in range(0,len(Aa)):
                a = Aa[i]                
                post_url = 'http://www.5ichai.com/phpwind/' + a.get('href')
                print (post_url)
        pdb.set_trace()               
        Atd=tr.find_all('td')            
        for i in range(0,len(Atd)):
            td=Atd[i]
            #print td.text.strip()
            f1.write(td.text.strip().encode('gb18030'))
            f1.write('\t')
        f1.write('\n')
    except:
        print (datename + "Error")    
f1.close
print ('Fin')
