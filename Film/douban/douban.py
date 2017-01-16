#coding=gb18030
import pdb
import requests
import sys
import time
from bs4 import BeautifulSoup
import datetime
import rppost

today = datetime.date.today()
filename = today.strftime("%Y-%m-%d")
print filename
#pdb.set_trace()

f1=open('./' + filename + '.txt','w')

i = "0"
new_url = "https://www.douban.com/group/467799/discussion?start=" + i
new_url = "https://www.douban.com/group/467799/discussion?start=0"
print new_url
rp = rppost.post(new_url)
soup = BeautifulSoup(rp, "html.parser",from_encoding = 'utf-8')
class_olt = soup.find(class_="olt")             #block
all_tr = class_olt.find_all("tr")
#print len(all_tr)
#Get the soup
for i in range(1,len(all_tr)):
        try:                       
                tr =all_tr[i]
                all_td = tr.find_all("td")
                href = all_td[0].a["href"]
                title  = all_td[0].a.text
                count = all_td[2].text
                time = all_td[3].text

                line = time + "\t" + count + "\t" + title + "\t" + href
                print line
                f1.write(line.encode("utf-8"))
                #pdb.set_trace()
        except:
                print ("err")
f1.close
