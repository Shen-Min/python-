# re.match用来匹配数据
# re.group用来获取匹配的数据

# 场景:匹配以itcast开头的语句,被匹配的语句itcast.cn
import re
match_obj = re.match('itcast','itcast.cn').group()
print(match_obj)