#coding=gb18030
import pdb
import requests
import sys
import time
from bs4 import BeautifulSoup

import datetime

begin = datetime.date(2016,7,15)
end = datetime.date.today()
d = begin
filename = end.strftime("%Y-%m-%d")
#pdb.set_trace()
f1=open('./sanxia/main' + filename + '.html','w')

delta = datetime.timedelta(days=1)
while d <= end:
    datename=d.strftime("%Y-%m-%d")
    print datename
    d += delta
    post_url="http://www.ctg.com.cn/inc/sqsk.php" #Get the Data
    data={
            'NeedCompleteTime2':datename,
    }
    try:
        rp=requests.post(post_url,data=data)
        ##It is very important!
        rp.encoding='gb18030'
        soup = BeautifulSoup(rp.content, "html.parser",from_encoding = 'gb18030')
        Atable = soup.find_all('table', {'class', 'top_t'})
        ##print Atable
        f1.write(datename + '  ')
        for i in range(1, len(Atable)):
            table=Atable[i]
            Atd=table.find_all('td')
            print len(Atd)
            if len(Atd)>0:
                td=Atd[0].text.encode('utf-8')
                f1.write(td)
            if len(Atd)>7:
                td=Atd[7].text.encode('utf-8')
                f1.write(td)
            if len(Atd)>5:
                td=Atd[5].text.encode('utf-8')
                f1.write(td)
            if len(Atd)>3:
                td=Atd[3].text.encode('utf-8')
                f1.write(td)
            if len(Atd)>1:
                td=Atd[1].text.encode('utf-8')
                f1.write(td)
            #pdb.set_trace()
            #for i in [0,7,5,3,1]:
            f1.write('  ')
        f1.write('\n')
    except:
        print (datename + "Error")    
f1.close
print ('Fin')
