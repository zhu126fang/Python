#coding=utf-8
import pdb
import requests
import sys
import time
from urllib import urlencode
from bs4 import BeautifulSoup

import datetime
import re
def len_zh(data):
    temp = re.findall('[^a-zA-Z0-9.-]+', data)
    count = 0
    for i in temp:
        count += len(i)
    return(count)

end = datetime.date.today()
filename = end.strftime("%Y-%m-%d")
f1=open('./mp4ba' + filename + '.html','w')
print filename
#pdb.set_trace()

post_url='http://www.mp4ba.com/index.php?' #Get the Data
print post_url
try:
    rp=requests.post(post_url)
    ##It is very important!
    rp.encoding='utf-8'
    soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'utf-8')    
    lasta = soup.find("a",class_="pager-last active")
    lastpage = int(lasta.text)
    print lastpage

    for i in range(1,lastpage):
        new_url = post_url + '&page=' + str(i)
        print new_url
        rp=requests.post(new_url)
        rp.encoding='utf-8'
        soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'utf-8')

        tbody = soup.find("tbody",class_="tbody")
        Atr = tbody.find_all('tr')
        print len(Atr)
        for i in range(0,len(Atr)):
            tr=Atr[i]
            Atd = tr.find_all('td')
            #print len(Atd)
            if len(Atd)==8:
                for i in range(0,len(Atd)):
                    text1 = Atd[i].text.strip()
                    if (i==2):
                        zh = len_zh(text1)
                        #print text1
                        #print zh
                        f1.write(text1.encode('utf-8').ljust(150+zh))
                    else:
                        f1.write(text1.ljust(15).encode('utf-8'))
            f1.write('\n')
    #pdb.set_trace()
except:
    print (filename + "Error")    
f1.close
print ('Fin')
