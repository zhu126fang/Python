#coding=gb18030
#UTF-8无BOM
import pdb
import requests
import sys
import time
from bs4 import BeautifulSoup

import datetime

begin = datetime.date(2016,7,1)
end = datetime.date(2016,7,9)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    datename=d.strftime("%Y-%m-%d")
    print datename
    d += delta

f1=open('./sanxia/main' + datename + '.html','w')

post_url="http://www.ctg.com.cn/inc/sqsk.php" #Get the Data
data={
	'NeedCompleteTime2':datename,
}

rp=requests.post(post_url,data=data)
##It is very important!
rp.encoding='gb18030'
soup = BeautifulSoup(rp.content, from_encoding = 'gb18030')
Atable = soup.find_all('table', {'class', 'top_t'})
#print Atable
f1.write(datename + '  ')
for i in range(1, len(Atable)):
    table=Atable[i]
    Atd=table.find_all('td')
    print len(Atd)

    for i in [0,7,5,3,1]:
        td=Atd[i].text.encode('utf-8')
        f1.write(td)
    f1.write('  ')
f1.write('\n')
    
##    f1.write('{\n"title":"' + Atd[0].text.encode('gb18030') + '",\n')
##    f1.write('"Value":[\n')
##    f1.write('"2":"' + Atd[7].text.encode('gb18030') + '",\n')
##    f1.write('"8":"' + Atd[5].text.encode('gb18030') + '",\n')
##    f1.write('"14":"' + Atd[3].text.encode('gb18030') + '",\n')
##    f1.write('"20":"' + Atd[1].text.encode('gb18030') + '"\n')
##    f1.write(']\n')
##    f1.write('}\n')
#pdb.set_trace()   

#pdb.set_trace() 

#print rp.headers['content-type']
#print (rp.text)
#f1.write(rp.content)
f1.close
print ('Fin')
