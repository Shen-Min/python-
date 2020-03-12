import pymysql
class Jdserver(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',port=3306,database = 'jing_dong',user = 'root',password = 'mysql',charset = 'utf8')

    def __del__(self):
        self.conn.close()

    def run(self):
        while True:
            print('1. 查询所有商品信息')
            print("2. 查询所有包含商品的分类")
            print("3. 添加新商品分类")
            print("4. 将所有商品价格加1000")
            print("5. 将所有笔记本的分类改为超级本")
            print("6. 根据id查询商品信息")
            print("7. 退出系统")

            action = input("请输入指令:")
            if action == '1':
                self.search_all_info()
            elif action == '2':
                self.search_cates_info()
            elif action == '3':
                self.add_cates()
            elif action == '4':
                self.update_price()
            elif action == '5':
                self.update_cates_info()
            elif action == '6':
                self.search_id_info()
            elif action == '7':
                break

    def search_all_info(self):
        cs = self.conn.cursor()
        sql = 'select * from goods;'
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()

        for temp in data:
            print(temp)

    def search_cates_info(self):
        cs = self.conn.cursor()
        sql = 'select distinct name from goods;'
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

    def add_cates(self):
        cs = self.conn.cursor()
        try:
            add_name = input('请输入要添加的商品分类:')
            sql = "insert into goods (name) values(%s)"
            cs.execute(sql,(add_name,))

            self.conn.commit()
        except Exception as e:
            print("异常:",e)

        cs.close()

    def update_price(self):
        cs = self.conn.cursor()
        sql= 'update goods set price = price + 1000 ;'
        cs.execute(sql)
        self.conn.commit()
        cs.close()

    def update_cates_info(self):
        cs = self.conn.cursor()
        sql = """update goods set cate_id = (select id from goods_cates where name = '超级本') where name like '%笔记本%';"""
        cs.execute(sql)
        self.conn.commit()
        cs.close()

    def search_id_info(self):
        cs =self.conn.cursor()
        user_id = input('请输入要查询信息的id:')
        sql = 'select * from goods where id = %s'
        cs.execute(sql,(user_id,))
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

def main():
    JD_server = Jdserver()
    JD_server.run()


if __name__ == '__main__':
    main()