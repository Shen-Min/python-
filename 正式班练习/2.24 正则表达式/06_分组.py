# | 相当于python中的or
# 	案例:匹配出163或者126的邮箱
import re
str1 = 'xiaohua@163.com'
str2 = 'xiaohua@126.com'

print(re.match("\w{4,20}@163\.com$", str1).group())
print(re.match("\w{4,20}@(163|126)\.com$", str1).group())
print(re.match("\w{4,20}@(163|126)\.com$", str2).group())

# ()还可以单独取出匹配的某一部分数据
# 	案例:取出邮箱的类型(只要163,126),后期可以编计用户那个邮箱用的多
print(re.match("\w{4,20}@(163|126)\.com", str1).group(1))
print(re.match("\w{4,20}@(163|126)\.com", str2).group(1))

str3 = "新年好2020python33"
print(re.match("新年好(2020)(python33)", "新年好2020python33").group(1))
print(re.match("新年好(2020)(python33)", "新年好2020python33").group(2))


# \num用来取第几组用()包裹的数据  \1取第一个内部的括号位置的值
# 格式(xxx)\1 :\1表示获取(xxx)的值
# 案例<html>hh</html>  # 这个一定是有字母,开始跟结束的字母必须一样

str = "<html>hh</html>"
print(re.match('<[a-zA-Z]+>.*</[a-zA-Z]+>', str).group())
print(re.match('<([a-zA-Z]+)>.*</\\1>', str).group())

str = "<html><body>hh</body></html>"
print(re.match('<([a-zA-Z]+)><([a-zA-Z]+)>.*</\\2></\\1>', str).group())





# 案例<html><body>hh</body></html>
str_data = "<html><body>hh</body></html>"

# 使用别名给分组取别名,了解一下
# 格式:(?P<别名>xxx)(?P=别名)
# 案例<html><body>hh</body></html>
# 提示问题没错
print(re.match('<(?P<name1>[a-zA-Z]+)><(?P<name2>[a-zA-Z]+)>.*</(?P=name2)></(?P=name1)>', str_data).group())
