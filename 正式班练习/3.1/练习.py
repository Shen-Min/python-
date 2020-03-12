from redis import *
sr = StrictRedis(host="120.24.188.143",port=6379,decode_responses=True)

sr.set("name1" ,"zs")

sr.set('name3','xiaohua')
print(sr.get('name1'))
