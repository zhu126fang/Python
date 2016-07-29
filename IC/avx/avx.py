#coding=utf-8
import pdb
import requests
import sys
import time
from urllib import urlencode
from bs4 import BeautifulSoup

import datetime

end = datetime.date.today()
filename = end.strftime("%Y-%m-%d")
f1=open('./avx' + filename + '.html','w')
print filename
#pdb.set_trace()

post_url='http://www.avx.com/contact-us/authorized/' #Get the Data
print post_url
try:
    rp=requests.post(post_url)
    ##It is very important!
    rp.encoding='utf-8'
    soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'utf-8')
    
    Asia = soup.find("table",class_="tablepress tablepress-id-12")
    Atr = Asia.find_all('tr')
    print len(Atr)
    #pdb.set_trace()

    for i in range(1,len(Atr)):
        tr=Atr[i]
        Atd = tr.find_all('td')
        print len(Atd)
        if len(Atd)>0:
            f1.write(Atd[0].text.ljust(50))
        if len(Atd)>1:
            f1.write(Atd[1].text.ljust(30))
        if len(Atd)>2:
            if (Atd[2].a is None):
                print 'None'
            else:
                print Atd[2].a['href']
                f1.write(Atd[2].a['href'].ljust(30))
        #pdb.set_trace()
        print(i)
        f1.write('\n')
except:
    print (filename + "Error")    
f1.close
print ('Fin')
