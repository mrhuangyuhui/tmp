# -*- coding: UTF-8 -*-
import string
from datetime import datetime, date

# 移除字符串左右两侧的空白符
def strippedString(str):
	return string.strip(str)

str = "  hello world  "
# print strippedString(str)

# 字符串转化为整数
num = "12345"
# print type(int(num))

# 字符串转化为日期时间
dt = datetime.strptime("2017-08-15 10:00", "%Y-%m-%d %H:%M")
# print type(dt)
# print dt
print date.today().strftime("%Y%m%d")

# url1 = r'<div align="center"><img src="http://cdn-yyj.4000916916.com/wx/wxExchange/prdDescImage/111500000016_20161122.jpg"></div>'
url1 = r'<div align="center"><img src="http://cdn-yyj.4000916916.com/wx/wxExchange/prdDescImage/'
url2 = "{}_{}".format("ttt", date.today().strftime("%Y%m%d"))
url3 = r'.jpg"></div>'
print url1+url2+url3