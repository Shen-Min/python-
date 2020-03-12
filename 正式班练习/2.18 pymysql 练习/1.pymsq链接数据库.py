import pymysql


def main():
    conn =pymysql.connect(host='127.0.0.1', port=3306, user='root', password='mysql', database='jing_dong', charset='utf8')
    cs = conn.cursor()
    cs.execute("SELECT * from goods;")
    data = cs.fetchall()
    for temp in data:
        print(temp)

    cs.close()
    conn.close()


if __name__ == '__main__':
    main()
