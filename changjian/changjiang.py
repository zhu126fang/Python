#coding=gb18030
#UTF-8 None BOM
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
   
datename=''
f1=open('./main' + datename + '.html','w')

#Get the list
post_url="http://www.cjmsa.gov.cn/vcms/classArticleListByPage.do" #Get the Data
data={
    'type':'active',
    'channelId':5,
    'classIds':67,
    'templateId':206,
    'page':1,
}

rp=requests.post(post_url,data=data)
##It is very important!
#rp.encoding='gb18030'
soup = BeautifulSoup(rp.content,"html.parser", from_encoding = 'utf-8')

Ali = soup.find_all('li', {'class', 'hui3'})
print len(Ali)

for i in range(0, len(Ali)):
    try:
        li=Ali[i]
        f1.write(li.span.text)          ##date
        f1.write('  ')
        post_url='http://www.cjmsa.gov.cn' +li.a.get('href')
        print  post_url
        rp=requests.post(post_url)
        rp.encoding='gb18030'
        soup = BeautifulSoup(rp.content,"html.parser", from_encoding = 'gb18030')
        #div= soup.find_all('div', {'class', 'nr1'})
        Atr= soup.find_all('tr')         ###Index is 7-17
        for i in range(7,17):
            tr=Atr[i]
            Atd=tr.find_all('td')            
            for i in [0,2,3]:
                td=Atd[i]
                f1.write(td.text.strip().encode('utf-8'))       ##data
                #pdb.set_trace()
                f1.write('  ')
        f1.write('\n')
    except:
        print ("Err")
        f1.write('\n')

    # for i in [0,7,5,3,1]:
        # td=Atd[i].text.encode('utf-8')
        # f1.write(td)
    # f1.write('  ')
# f1.write('\n')

f1.close
print ('Fin')
