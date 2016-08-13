##v0.1说明
###fid2.py
- 以当前的日期创建文件  
- 条目格式<tr class="tr3 t_one" align="center">  
- 抓取格式Atr = soup.find_all("tr",class_="tr3 t_one")  
- 抓取1-100页的内容  
- [数量][地址][标题]  

###sortfid7.py
- 按行读取文件 for line in f.readlines():  
- 根据分隔符号分割行 l_line = line.split('|')  
- 首行字符串转换为数字 l_line[0] = int(l_line[0].strip())  
- 二维数组按照首行元素排序 a2.sort(reverse = True)  

##v0.2说明(完整获取后才能开始排序)
###fid2a.py  
- 合并fid2.py 和 sortfid2.py的功能  
