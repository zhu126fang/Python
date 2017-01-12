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

post_url="http://www.huhupan.com/index_1000.html"       #get the data
rp = rppost.post(post_url)

soup = BeautifulSoup(rp, "html.parser",from_encoding = 'utf-8')
all_block = soup.find_all(class_="block")                                       #get the block
print len(all_block)

for i in range(1,len(all_block)):
        block = all_block[i]
        try:
                category = block.h2.a.text              #if encode('utf-8') print will messy code
        except:
                category ="err"

        try:
                preview = block.find(class_="preview").text
        except:
                preview = "err"

        try:
                preem = block.find(class_="preem").a["href"]
        except:
                preem = "err"        

        try:
                viewimg_title  = block.find(class_="viewimg").a["title"]
                viewimg_href = block.find(class_="viewimg").a["href"]

                url_name = viewimg_href.split("/")[-1].split(".")[0]
                new_url = "http://www.huhupan.com/e/extend/down/?id=" + url_name
                print new_url
                rp = rppost.post(new_url)
                soup = BeautifulSoup(rp, "html.parser",from_encoding = 'utf-8')
                all_btn = soup.find_all(class_="meihua_btn")
                for i in range(1,len(all_btn)):
                        print all_btn[i]["href"]
                all_bdypas = soup.find("input",{"id":re.compile("bdypas\d+")})
                for i in range(1,len(all_btn)):
                        print all_bdypas[i]
                #all_class = soup.find_all(class_="meihua_btn")
                #print len(all_class)

        except:
                viewimg_href = "err"
                viewimg_title  = "err"

        #print (category)
        #print (viewimg_title)
        #print (viewimg_href)
                
        f1.write(viewimg_href.encode('utf-8') + "\n")
f1.close
print ('Finish')
