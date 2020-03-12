import pymysql
class Students(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',port=3306,database = 'python33',user = 'root',password = 'mysql',charset = 'utf8')

    def __del__(self):
        self.conn.close()

    def run(self):
        while True:
            print('1、打印所有学生的姓名、各科成绩')
            print("2、查询指定姓名学生的各科成绩")
            print("3、添加新的学生的考试信息 ")
            print("4、输出成绩总分前3名的学生姓名、各科成绩、总分数")

            action = input("请输入指令:")
            if action == '1':
                self.print_student_info()
            elif action == '2':
                self.search_student_info()
            elif action == '3':
                self.add_student_info()
            elif action == '4':
                self.search_first3_student_info()

    def print_student_info(self):
        cs = self.conn.cursor()
        sql = 'select name,chinese,english,math from students;'
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

    def search_student_info(self):
        cs = self.conn.cursor()
        name = input("请输入要查询的学生姓名:")
        sql = 'select chinese,english,math from students where name = %s;'
        cs.execute(sql,(name,))
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

    def add_student_info(self):
        cs = self.conn.cursor()
        try:
            add_name = input('请输入要添加的姓名:')
            add_chinese = input('请输入语文成绩:')
            add_english = input('请输入英语成绩:')
            add_math = input('请输入数学成绩:')
            sql = "insert into students (name,chinese,english,math) values(%s,%s,%s,%s)"
            cs.execute(sql,(add_name,add_chinese,add_english,add_math))

            self.conn.commit()
        except Exception as e:
            print("异常:",e)

        cs.close()

    def search_first3_student_info(self):
        cs = self.conn.cursor()
        sql = 'select name,chinese,english,math,chinese+english+math total  from students order by total desc limit 0, 3;'
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

def main():
    student = Students()
    student.run()


if __name__ == '__main__':
    main()