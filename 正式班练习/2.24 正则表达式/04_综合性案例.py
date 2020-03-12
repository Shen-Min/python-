#  ^ 以什么开始 python语言的match是自动添加的,其他语言不是这样,所以必须添加
# $以什么结尾


# "^xxx$"  $ 这个就是匹配到尾


# 匹配变量名是否有效
# 匹配规则: 字母_开头, 匹配的数据: names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]
names = ["age", "_age", "1age", "age1", "a_age", "age_1_", "age!", "a#123", "------"]
import re

for i  in names:
    result = re.match("^[a-zA-Z_][a-zA-Z0-9_]*$",i )
    if result:
        print("成功",result.group())

    else:
        print('失败',i)

