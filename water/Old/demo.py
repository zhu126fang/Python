#coding=utf-8
import requests
from bs4 import BeautifulSoup

get_url="http://www.szhec.gov.cn/pages/szepb/kqzl/TGzfwHjKqzlzs.jsp?FLAG=FIRSTFW"#获取hash值
post_url="http://www.szhec.gov.cn/pages/szepb/kqzl/TGzfwHjKqzlzs.jsp" #获取空气质量时报
html=requests.get(get_url)
#使用beautiful解析网页，获取hash值
html_soup=BeautifulSoup(html.text,"html.parser")
hash=html_soup.select("input[name=hash]")
hash=hash[0].get('value')
#构造data
data={

'hash':hash,
'FROM_SELF':'true',
'q_JCRQ':'2016-04-01',
'q_SDATE':'00',
'q_JCDW':'',
'q_JCDW_text':'',

}
#至此已经正确获取了控制质量时报的信息
tqHtml=requests.post(post_url,data=data)
print tqHtml.text