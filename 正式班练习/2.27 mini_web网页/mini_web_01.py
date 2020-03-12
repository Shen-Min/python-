# 升级的思想,主函数像书的目录一样,
# 一个函数一个功能,方便后期代码的查看跟管理



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

		response_body = index()

	elif file_path == "/center.html":
		response_body = center()

	elif file_path == "/center.html":

		response_body = center()
	elif file_path == "/center.html":

		response_body = center()
	elif file_path == "/center.html":

		response_body = center()
	elif file_path == "/center.html":

		response_body = center()

	else:
		# 组一个响应格式的数据
		# 响应行
		response_line = "http/1.1 404 not found \r\n"

		# 打开前端的界面
		response_body = "not page is show!"

	return response_line, response_head, response_body


def center():
	# 打开前端的界面
	response_body = "center page is show2020!"

	return response_body


def index():
	# 打开前端的界面
	response_body = "index page is show!"

	return response_body
