# 查询结果
# 	search 不会从头开始匹配,只要匹配到数据就结束
# 	案例:匹配出文章阅读的次数中的次数
# 	数据:"阅读次数为 9999"

import re
str= "阅读次数为 9999"
print(re.match('\w+\s(\d+)', str).group())
print(re.match('\w+\s(\d+)', str).group(1))

print(re.search('\d+', str).group())



# 查询结果集
# findall
# 案例: 统计出python、c、c + +相应文章阅读的次数
# 数据: "python = 9999, c = 7890, c++ = 12345"

str = "python = 9999, c = 7890, c++ = 12345"
print(re.findall("\d+", str))

# 替换数据
# sub
# 案例: 将匹配到的阅读次数换成998
# 数据: "python = 997"

str = "python = 997"
print(re.sub("\d+", "998", str))