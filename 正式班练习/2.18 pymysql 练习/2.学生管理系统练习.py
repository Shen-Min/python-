from pymysql import connect
class StudentManagement(object):
    def __init__(self):
        self.conn = connect(host = "localhost",port = 3306,user = 'root',password = 'mysql',database = 'student_manage',charset = 'utf8')

    def run(self):
        while True:
            str = """---------------------------
		学生管理系统 V1.0
1:添加学生
2:删除学生
3:修改学生
4:查询学生
5:显示所有学生
6:退出系统
---------------------------"""
            print(str)

            action = input('请输入指令:')
            if action == '1':
                self.add_stdent_info()
            elif action == '2':
                self.delete_student_info()
            elif action == '3':
                self.update_student_info()
            elif action == '4':
                self.search_student_info()
            elif action == '5':
                self.show_student_info()
            elif action == '6':
                break
        self.conn.close()

    def add_stdent_info(self):
        cs = self.conn.cursor()
        name = input('请输入学生姓名:')
        age = input('请输入学习年龄:')
        tel =input('请输入学生电话:')
        sql = 'insert into student(name,age,tel) value (%s,%s,%s)'
        cs.execute(sql,(name,age,tel))
        self.conn.commit()
        cs.close()

    def delete_student_info(self):
        cs = self.conn.cursor()
        student_code = input('请输入要删除的学生学号:')
        sql = "delete from student where student_code = %s"
        cs.execute(sql,(student_code,))
        self.conn.commit()
        cs.close()

    def update_student_info(self):
        cs = self.conn.cursor()
        delete_student_code= input('请输入要修改的学生学号:')
        name = input('请输入修改的名字:')
        age  = input('请输入要修改的年龄:')
        tel  = input('请输入要修改的电话:')
        sql = "update student set name = %s,age = %s,tel =%s where student_code = %s"
        cs.execute(sql, (name,age,tel,delete_student_code))
        self.conn.commit()
        cs.close()

    def search_student_info(self):
        cs = self.conn.cursor()
        search_student_code = input('请输入要查询的学生学号:')
        sql = "select * from student where student_code = %s"
        cs.execute(sql,(search_student_code,))
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)

    def show_student_info(self):
        cs = self.conn.cursor()
        sql = "select * from student;"
        cs.execute(sql)
        data = cs.fetchall()
        cs.close()
        for temp in data:
            print(temp)


def main():
    student_manage = StudentManagement()
    student_manage.run()


if __name__ == '__main__':
    main()