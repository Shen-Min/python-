# 升级的思想,一个程序中if...else太多了以后也不便于管理,我们以后可以考虑使用字典




# 根据不同的地址返回不同响应体
from pymysql import connect


# 让我们的主函数简洁,像书的目录一样
# 一个函数一个功能

def application(file_path):
	# 响应行
	response_line = "http/1.1 200 ok \r\n"
	# 响应头
	response_head = ""
	# if file_path == "/index.html":
	#
	# 	response_body = index()
	#
	# elif file_path == "/center.html":
	#
	# 	response_body = center()
	#
	#
	# else:
	# 	# 组一个响应格式的数据
	# 	# 响应行
	# 	response_line = "http/1.1 404 not found \r\n"
	#
	# 	# 打开前端的界面
	# 	response_body = "not page is show!"

	# 如果if...else超过三个以上,可以考虑使用字典
	try:
		# 1.定义一个访问路径与执行页面函数的字典
		url_dict = {"/index.html": index, "/center.html": center, "/login.html": login,"regedit.html":regedit}
		# 2.通过不同的路径得到不同的执行页面的函数
		response_body = url_dict[file_path]()
	except Exception as e:
		print("错误:", e)
		# 组一个响应格式的数据
		# 响应行
		response_line = "http/1.1 404 not found \r\n"

		# 打开前端的界面
		response_body = "not page is show!"

	return response_line, response_head, response_body
def regedit():
	return "regedit page is show!"

def login():
	return "login page is show!"


def center():
	# 打开前端的界面
	response_body = "center page is show2020!"

	return response_body


def index():
	# 打开前端的界面
	response_body = "index page is show!"

	return response_body
