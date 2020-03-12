# 1.初始化tcp
# 2.绑定端口及复用
# 3.监听
# 4.循环接收客户端请求
# 5.处理客户端请求
# 6.关闭


# 面向对象
# 1.先定义一个对象WebServer对象
# 2.行为分析(函数/方法)
# 3.初始化方法
# 3.1.初始化tcp
# 3.2.绑定端口及复用
# 3.3.监听
# 4.运行服务器方法
# 4.1.循环接收客户端请求
# 5.客户端处理
# 5.1.处理客户端请求
import socket
import threading

import sys

import mini_web_10


class WebServer(object):
	# 初始化
	def __init__(self, port):
		# 1. 初始化socket
		self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# 2.绑定及复用端口
		self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
		self.socket_server.bind(("", port))

		# 3.监听
		self.socket_server.listen(128)

	# 运行服务器
	def run_server(self):
		# 4.循环接收客户端
		while True:
			client, address = self.socket_server.accept()

			# 5.处理客户端请求
			# self.client_exec(client) # 这里的代码有可能会响应的时间很长,为了可以及时响应下个客户端,我们把响应时间长的代码放到一个线程中
			threading.Thread(target=self.client_exec, args=(client,)).start()

		# 6.关闭
		socket_server.close()

	# 客户端处理
	def client_exec(self, client):
		# 1.得到请求的数据
		# 2.如果请求的时候有数据,那么我们得到请求的资源路径
		# 3.根据不同的资源路径返回不同的响应体
		# 4.关闭


		# 1.得到请求的数据
		recv_data = client.recv(1024)
		# 要对请求过来的数据进行判断,千万不相信别人传给你的数据
		# 如果传过来的数据为空,说明不是游览器访问,我们可以直接断开连接
		if recv_data:
			# 说明请求有数据
			# 1.得到解析后的数据
			# 2.得到请求行里面的请求地址

			# 1.得到解析后的数据
			data_decode = recv_data.decode('utf-8')
			# print("请求数据:",data_decode)
			# GET /index.html HTTP/1.1
			split_list_data = data_decode.split(" ")
			# print("split分的数据:",split_list_data)
			# 获取我们的资源路径,我们防止有可能不按http协议发的数据,
			# 如果不是http协议的请求,我们直接断开连接,返回
			try:
				file_path = split_list_data[1]

				print("得到请求的资源路径:", file_path)
				# 如果请求的资源路径是/那么我们直接把/改成/index.html,让/请求的请求展示/index.html的内容
				if file_path == "/":
					file_path = "/index.html"
			except Exception as e:
				print("异常:", e)
				# 如果异常了,断开连接返回
				client.close()
				return  # 让代码不向下执行

		else:
			# 说明请求没有数据,直接断了连接,返回
			client.close()
			return  # 让我们代码不要向下走了,这个很重要

		# 需要对代码进行重构
		# 重构的原因,是因为图片太多了以后,工作量会相当大
		# 我们可以根据资源的特性进行处理,如果web程序员后期需要更改的资源(.html)可以称为动态资源,动态 资源需要一个一个处理
		# 如果后期不需要web程序进行更改,如果,web程序员改不了的资源称为静态资源(.png,.jpeg,.mp3,mp4,.avi),静态我们可以统一的处理

		# 判断是否是.html结尾的
		if file_path.endswith(".html"):
			# 说明后期是.html,我们可以认为是动态资源,一个一个处理
			# 动态资源一个一个处理
			# 我们可以把公共的部分抽取到if的外部,那么每次走if之前都会先走公共的部分
			# 响应行
			response_line = "http/1.1 200 ok\r\n"
			# 响应头
			response_head = ""
			# 空行
			response_empty = "\r\n"

			# 根据不同的地址返回一个响应内容
			# 把这个动态资源的代码单独抽取出来方便最后的维护管理

			#
			# if file_path == "/index.html":
			#
			# 	# 返回index网页的内容
			# 	# 响应组一个响应的格式的内容返回
			#
			# 	# 响应体
			# 	response_body = "index page is show,name:oldyang"
			#
			#
			#
			# elif file_path == "/center.html":
			# 	# 响应组一个响应的格式的内容返回
			#
			# 	# 响应体
			# 	response_body = "center page is show!"
			#
			#
			# elif file_path == "/login.html":
			#
			# 	# 响应体
			# 	# 使用文本操作
			# 	# 展示网页文本最大的区别在于文本直接给响应体
			# 	# 网页需要使用with open 打开以后给我们的响应体
			# 	with open("./post.html", encoding='utf-8') as f:
			# 		content = f.read()
			# 	# 把读完的数据赋值给响应体
			# 	response_body = content
			#
			# # 京东页面展示
			# elif file_path == "/jd.html":
			# 	with open("./jd.html", encoding='utf-8') as f:
			# 		content = f.read()
			#
			# 	response_body = content  # 响应体就是京东的页面
			#
			# else:
			# 	# 当用户 输入的地址不在上面是不是要做处理,有可能输入/xxx.html
			# 	# 网页没有这个网页处理
			# 	# 响应组一个响应的格式的内容返回
			# 	# 响应行
			# 	response_line = "http/1.1 404 not found\r\n"
			#
			# 	# 响应体
			# 	response_body = "not page is show!"

			# 所有动态资源的处理都交给mini_web_10这个文件中的application方法执行
			response_line, response_body = mini_web_10.application(file_path)

			# 组成响应格式数据
			response_data = response_line + response_head + response_empty + response_body

			# 发送数据
			client.send(response_data.encode("utf-8"))  # 注意编码

		else:
			# 有可能找不到前端给的资源,我们需要进行异常处理
			try:
				# 说明是静态资源,做统一处理
				# 如果图片一张图片,那么我们需要返回图片的内容,必须按照响应的格式
				# 响应行
				response_line = "http/1.1 200 ok\r\n"
				# 响应头
				# 千万不要加中文的头
				response_head = ""
				# 空行
				response_empty = "\r\n"

				# 响应体
				# 使用文本操作
				# 展示网页文本最大的区别在于文本直接给响应体
				# 网页需要使用with open 打开以后给我们的响应体
				# rb二进制方式读取
				# 晚上写代码的时候一定要注意
				# with open("./2.jpg", 'rb') as f:
				# 	content = f.read()

				# 在工作中项目里的路径尽量写相对路径,你的代码是要上传到服务器,你服务器的路径跟你电脑的路径有可能是不相同的,使用绝对路径会有问题
				with open(".%s" % file_path, 'rb') as f:
					content = f.read()
				# 把读完的数据赋值给响应体
				response_body = content

				# 组成响应格式数据
				# 图片处理的时候需要会部转成二进制
				response_data = response_line.encode("utf-8") + response_head.encode("utf-8") + response_empty.encode(
					"utf-8") + response_body

				# 发送数据
				# 响应的内容已经是二进制,那么不需要再编码
				client.send(response_data)  # 注意编码
			except Exception as e:
				print("异常", e)
				# 资源找不到,返回404的信息
				# 响应行
				response_line = "http/1.1 404 not found\r\n"
				# 响应头
				response_head = ""
				# 空行
				response_empty = "\r\n"
				# 响应体
				# 如果返回的是图片,这个文字是不是显示
				response_body = "not path is find!"

				# 组成响应格式数据
				response_data = response_line + response_head + response_empty + response_body

				# 发送数据
				client.send(response_data.encode("utf-8"))  # 注意编码

		# 4关闭
		client.close()


def main():
	"""主函数"""
	# 面向对象适合大型项目 ,多人合作开发的时候会效果更明显
	# 从命令行得到一个端口信息
	# 标准的格式:python3 文件名 端口
	# 进行异常的处理
	try:
		cmd_argv = sys.argv
		# 返回的是一个列表,第一个永远是当前的文件名,第二个是端口
		port_str = cmd_argv[1]

		# 字符串转成int
		port = int(port_str)

		# 初始化web服务器
		server = WebServer(port)

		# 开启web服务
		server.run_server()
	except Exception as e:
		print("亲,您的格式不正确:python3 文件名 端口号!")


if __name__ == '__main__':
	main()
