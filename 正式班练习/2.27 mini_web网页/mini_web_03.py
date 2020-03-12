# 升级的思想,装饰器得到原先函数的引用,通过装饰器传参传入原先函数对应的路径,我们就可以自动的生成一个路径的对应字典
# 使用装饰器传参,完成字典的自动生成

# 根据不同的地址返回不同响应体
from pymysql import connect

# 定义一个空的字典
# url_dict = {}
url_dict = dict()

# 路由功能:
# 装饰器传参完成了flask的路由功能
# 可以使用装饰器传参
def set_url(url):
	# 使用装饰器
	def set_fun(func):
		def call_fun(*args, **kwargs):
			print("添加权限")
			return func(*args, **kwargs)

		print("原先的函数:", func)
		print("原先的函数对应的url:", url)
		# 装饰一次生成一个字典数据
		url_dict[url] = func

		return call_fun

	return set_fun


# 让我们的主函数简洁,像书的目录一样
# 一个函数一个功能

def application(file_path):
	# 响应行
	response_line = "http/1.1 200 ok \r\n"
	# 响应头
	response_head = ""

	# 如果if...else超过三个以上,可以考虑使用字典
	try:
		# 1.定义一个访问路径与执行页面函数的字典
		# 字典自动生成了,不需要手动再去生成
		# url_dict = {"/index.html": index, "/center.html": center, "/login.html": login, "regedit.html": regedit}
		print("自动生成的字典:",url_dict)

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

# /index.html regedit

# 路由可以控制当前的页面是否可以展示
@set_url("/regedit.html")
def regedit():
	return "regedit page is show 2020!"


@set_url("/login.html")
def login():
	return "login page is show!"


def center():
	# 打开前端的界面
	response_body = "center page is show2020!"

	return response_body

@set_url("/index.html")
def index():
	# 打开前端的界面
	response_body = "index page is show!"

	return response_body
