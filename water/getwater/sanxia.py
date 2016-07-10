#coding=gb18030
#UTF-8无BOM
import requests
import sys
import time
from bs4 import BeautifulSoup

import datetime
begin = datetime.date(2016,6,1)
end = datetime.date(2016,7,9)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    datename=d.strftime("%Y-%m-%d")
    print datename
    d += delta

    f1=open('./sanxia/main' + datename + '.html','w')

    post_url="http://www.ctg.com.cn/inc/sqsk.php" #获取三峡水位数据
    data={
        'NeedCompleteTime2':datename,
    }
    #至此已经正确获取了控制质量时报的信息
    rp=requests.post(post_url,data=data)
    ##It is very important!
    rp.encoding='gb18030'   

    #print rp.headers['content-type']
    #print (rp.text)
    f1.write(rp.content)
    f1.close
    print ('Fin')
