# 升级的思想,装饰器得到原先函数的引用,通过装饰器传参传入原先函数对应的路径,我们就可以自动的生成一个路径的对应字典
# 使用装饰器传参,完成字典的自动生成

# 根据不同的地址返回不同响应体
import json
import re
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
		print("自动生成的字典:", url_dict)

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


####################################################上面是框架###################################################

# 展示页面
# 1.写一个函数
# 2.通过装饰器传参注册到字典中

@set_url("/index.html")
def index():
	# 1.打开前端
	# 2.得到数据库数据
	# 3.数据库的数据跟前端拼接在一起
	# 4.返回拼接后的数据

	# 1.打开前端
	with open("./templates/index.html", encoding="utf-8") as f:
		content = f.read()

	# 2.数据库数据得到
	# 1. 从数据库得到数据
	# 1.1连接数据库
	# 创建Connection连接
	conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
	# 获得Cursor对象
	cs1 = conn.cursor()

	# 1.2 执行查询的sql语句
	cs1.execute("select * from info;")
	# 得到数据库的数据
	data = cs1.fetchall()

	# 1.3 关闭
	cs1.close()
	conn.close()

	# 测试一下得到的数据
	for temp in data:
		print(temp)

	# 被替换的字符
	row_str = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
        </td>
        </tr>"""

	# 我们现在替换的数据是数据库中有多少数据就展示 多少数据
	# 定义一个整体展示的字符串变量
	table_str = ""
	for temp in data:
		table_str += row_str % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])  # 根据数据库的条数进行拼接

	# 替换前端的模板代码(只有页面,没有数据)
	new_hmtl_content = re.sub("\{%content%\}", table_str, content)  # content这个被替换的网页

	return new_hmtl_content



# 第一次返回页面
@set_url("/center.html")
def center():
	with open("./templates/center_2.html",encoding="utf-8") as f:
		content = f.read()

	return content


# 第二次返回数据
# 给个数据

@set_url("/center_data.html")
def center_data():
	# [{},{},{}]
	#  //一行的数据是一个字典,把每一行加到一个列表,这个json格式的数据
	# 1. 从数据库得到数据
	# 1.1连接数据库
	# 创建Connection连接
	conn = connect(host='localhost', port=3306, database='stock_db', user='root', password='mysql', charset='utf8')
	# 获得Cursor对象
	cs1 = conn.cursor()
	cs1.execute("set names utf8;")
	# 1.2 执行查询的sql语句
	cs1.execute(
		"""select info.code,info.short,info.chg,info.turnover,info.price,info.highs,focus.note_info from info inner join focus on info.id = focus.info_id;""")
	# 得到数据库的数据
	data = cs1.fetchall()

	# 1.3 关闭
	cs1.close()
	conn.close()

	# 把数据拼成前端需要json格式返回,这个需要思考
	# 定义一个空的列表
	json_list = list()
	# 通过数据的循环添加字典的信息
	for temp in data:
		# 生成一个字典添加到列表中
		json_dict = dict()

		json_dict['code'] = temp[0]
		json_dict['short'] = temp[1]
		json_dict['chg'] = temp[2]
		json_dict['turnover'] = temp[3]
		json_dict['price'] = str(temp[4]) # 小数转json时需要先转成字符串再转成json数据
		json_dict['highs'] = str(temp[5])
		json_dict['note_info'] = temp[6]

		# 添加到列表中
		json_list.append(json_dict)

	print("生成的对象数据:", json_list)

	# 返回python中的对象转成json格式的字符串返回
	json_str = json.dumps(json_list) # 转成json的时候如果有小数,是需要特殊处理的

	return json_str