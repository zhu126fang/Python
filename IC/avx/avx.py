#coding=gb18030
#UTF-8 BOM
import pdb
import requests
import sys
import time
from urllib import urlencode
from bs4 import BeautifulSoup

import datetime

end = datetime.date.today()
filename = end.strftime("%Y-%m-%d")
f1=open('./Home' + filename + '.html','w')
print filename
#pdb.set_trace()

post_url='http://www.avx.com/contact-us/authorized/' #Get the Data
print post_url
try:
    rp=requests.post(post_url)
    ##It is very important!
    rp.encoding='gb18030'
    soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
    
    Adiv = soup.find_all("div",class_="dataTables_wrapper no-footer")
    div = Adiv[3]
    pdb.set_trace()
    #print table
    
    Atr = table.find_all('tr')
    #pdb.set_trace()

    for i in range(2,len(Atr)):
        tr=Atr[i]
        Atd = tr.find_all('td')
        post_url = 'http://119.97.201.28:8087/'+ Atd[0].a.get('href')
        rp=requests.post(post_url)
        ##It is very important!
        rp.encoding='gb18030'
        soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
        print post_url
        pdb.set_trace()
        
        for i in range(0,len(Atd)):
            td = Atd[i]
            tdtext = td.text.encode('utf-8').strip()
            #print len(tdtext)
            f1.write(tdtext)
            if len(tdtext)<34:
                f1.write('\t')
            if len(tdtext)<33:
                f1.write('\t')
            #pdb.set_trace()
            f1.write('\t')            
        f1.write('\n')
except:
    print (filename + "Error")    
f1.close
print ('Fin')
