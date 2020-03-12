import pymysql
class JDserver(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')
        self.cs = self.conn.cursor()

    def __enter__(self):
        self.cs.execute("SELECT * from goods;")
        data = self.cs.fetchall()
        for temp in data:
            print(temp)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing connection...")
        self.cs.close()
        self.conn.close()

jd = JDserver()
with jd:
    jd.cs.execute("select * from goods_brands")
    for tmp in jd.cs.fetchall():
        print(tmp)
