#coding=utf-8
import requests
from bs4 import BeautifulSoup

get_url="http://www.szhec.gov.cn/pages/szepb/kqzl/TGzfwHjKqzlzs.jsp?FLAG=FIRSTFW"#��ȡhashֵ
post_url="http://www.szhec.gov.cn/pages/szepb/kqzl/TGzfwHjKqzlzs.jsp" #��ȡ��������ʱ��
html=requests.get(get_url)
#ʹ��beautiful������ҳ����ȡhashֵ
html_soup=BeautifulSoup(html.text,"html.parser")
hash=html_soup.select("input[name=hash]")
hash=hash[0].get('value')
#����data
data={

'hash':hash,
'FROM_SELF':'true',
'q_JCRQ':'2016-04-01',
'q_SDATE':'00',
'q_JCDW':'',
'q_JCDW_text':'',

}
#�����Ѿ���ȷ��ȡ�˿�������ʱ������Ϣ
tqHtml=requests.post(post_url,data=data)
print tqHtml.text