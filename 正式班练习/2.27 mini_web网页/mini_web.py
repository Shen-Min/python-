# 根据不同的地址返回不同响应体
from pymysql import connect

# 让我们的主函数简洁,像书的目录一样
# 一个函数一个功能

def application(file_path):
	# 响应行
	response_line = "http/1.1 200 ok \r\n"
	# 响应头
	response_head = ""
	if file_path == "/index.html":

		# 打开前端的界面
		response_body = "index page is show!"
		# 1. 从数据库得到数据
		# 1.1连接数据库
		# 创建Connection连接
		conn = connect(host='localhost', port=3306, database='jing_dong', user='root', password='mysql', charset='utf8')
		# 获得Cursor对象
		cs1 = conn.cursor()

		# 1.2 执行查询的sql语句
		cs1.execute("")
		# 得到数据库的数据
		data = cs1.fetchall()

		# 1.3 关闭
		cs1.close()
		conn.close()

		# 1. 从数据库得到数据
		# 1.1连接数据库
		# 创建Connection连接
		conn = connect(host='localhost', port=3306, database='', user='root', password='mysql', charset='utf8')
		# 获得Cursor对象
		cs1 = conn.cursor()

		# 1.2 执行查询的sql语句
		cs1.execute("")
		# 得到数据库的数据
		data = cs1.fetchall()

		# 1.3 关闭
		cs1.close()
		conn.close()
		# 1. 从数据库得到数据
		# 1.1连接数据库
		# 创建Connection连接
		conn = connect(host='localhost', port=3306, database='', user='root', password='mysql', charset='utf8')
		# 获得Cursor对象
		cs1 = conn.cursor()

		# 1.2 执行查询的sql语句
		cs1.execute("")
		# 得到数据库的数据
		data = cs1.fetchall()

		# 1.3 关闭
		cs1.close()
		conn.close()

	elif file_path == "/center.html":

		# 打开前端的界面
		response_body = "center page is show2020!"
		# 1. 从数据库得到数据
		# 1.1连接数据库
		# 创建Connection连接
		conn = connect(host='localhost', port=3306, database='', user='root', password='mysql', charset='utf8')
		# 获得Cursor对象
		cs1 = conn.cursor()
		
		# 1.2 执行查询的sql语句
		cs1.execute("")
		# 得到数据库的数据
		data = cs1.fetchall()
		
		# 1.3 关闭
		cs1.close()
		conn.close()

	elif file_path == "/login.html":

		# 打开前端的界面
		with open("./post.html", 'r') as f:
			response_body = f.read()

	elif file_path == "/regedit.html":
		response_body = 'regedit page is show!'

	else:
		# 组一个响应格式的数据
		# 响应行
		response_line = "http/1.1 404 not found \r\n"

		# 打开前端的界面
		response_body = "not page is show!"

	return response_line, response_head, response_body
