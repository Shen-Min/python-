# \进行转义
# 在正则特殊的符号, 想以字符串的形式使用使用转义
# 匹配出163的邮箱地址，且 @ 符号之前有4到20位字符, 以.com结尾
import re
mail = "xiaohua@163.com"
print(re.match('\w{4,20}@163\.com', mail).group())
print(re.match('\w{4,20}@163\.com$', mail).group())