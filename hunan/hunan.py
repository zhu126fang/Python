#coding=gb18030
#UTF-8鏃燘OM
import pdb
import requests
import sys
import time
from bs4 import BeautifulSoup

import datetime

f1=open('./dongting.html','w')
f2=open('./shashi.html','w')
title='时间		河名 	站名 	时间 	水位	较前日	流量	警戒 	最高	发生时间 	所在县 控制面积'
f1.write(title)
f1.write('\n')
f2.write(title)
f2.write('\n')
begin = datetime.date(2016,7,11)
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

    post_url='http://61.187.56.156/wap/zykz_BB2.asp?nian=' + nian + '&yue=' + yue + '&ri=' + ri + '&shi=21%3A00' #Get the Data
    print post_url
    try:
        rp=requests.post(post_url)
        ##It is very important!
        rp.encoding='gb18030'
        soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
        #Atable = soup.find_all('table', {'class', 'top_t'})
        Atr = soup.find_all('tr')      
        f1.write(datename + '\t')
        f2.write(datename + '\t')
        #for i in range(20, len(Atr)):
        tr=Atr[22]
        Atd=tr.find_all('td')            
        for i in range(0,len(Atd)):
            td=Atd[i]
            #print td.text.strip()
            f1.write(td.text.strip().encode('gb18030'))
            f1.write('\t')
        f1.write('\n')
        ##shashi
        tr=Atr[25]
        Atd=tr.find_all('td')            
        for i in range(0,len(Atd)):
            td=Atd[i]
            #print td.text.strip()
            f2.write(td.text.strip().encode('gb18030'))
            f2.write('\t')
        f2.write('\n')
        #pdb.set_trace()
    except:
        print (datename + "Error")    
f1.close
f2.close
print ('Fin')
