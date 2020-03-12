# 1.初始化tcp服务器
# 2. 循环接收客户端的请求
# 3. 处理客户端的请求
# 4.关闭

# 一个函数一个功能
# 类是相关函数的集合,管理相关的函数
# 面向对象的时候要合理的使用魔法方法
import socket
import threading

import mini_web_flask


class WebServer(object):
	def client_exec(self, client):
		"""
		客户端的处理

		:param client:
		:return:
		"""

		# 1.得到请求的路径
		# 2.根据不同的地址返回不同的响应内容
		# 3. 关闭

		# 1.1 得到请求的数据
		# 1.2 判断当前是否有数据
		# 1.2.1如果有数据,那么解析
		# 1.2.2如果没有数据那么直接退出

		# 千万不要相信别人给人数据*******
		recv_data = client.recv(1024)
		if recv_data:
			# 说明有数据
			# 解码数据
			data = recv_data.decode("utf-8")
			# 得到对应的地址
			try:
				split_data = data.split(" ", maxsplit=2)
				# 得到路径
				file_path = split_data[1]
				# 判断当前的路径如果是/那么定位到/index.html
				if file_path == "/":
					file_path = "/index.html"



			except Exception as e:
				print("解析地址的地址出错:", e)
				# 直接 退出
				client.close()
				return


		else:
			# 说明没有数据
			# 直接退出
			client.close()
			return

		# 静态资源一种动态资源
		# 静态资源后端程序不会去更改的资源就是静态资源,mp3,mp4,jpg,png,css,js,
		# 静态的处理都是统一,二进制读取返回
		# 动态资源,我们可以会改,一般.html的内容我们有可能会进行更改的

		# 根据资源的特性进行相应的处理,静态资源统一处理,动态资源判断处理
		# 动态的资源后缀是.html
		# 根据不同的路径返回不同的响应体
		if file_path.endswith(".html"):
			# 动态资源
			# 单独处理
			# 空行
			empty_line = "\r\n"

			# 响应体
			response_line, response_head, response_body = mini_web_flask.application(file_path)

			# 响应的内容
			response_content = response_line + response_head + empty_line + response_body

			# 发送响应格式的数据
			client.send(response_content.encode("utf-8"))
		else:
			# 静态资源
			# 统一处理

			try:
				# 响应的格式
				# 响应行
				response_line = "http/1.1 200 ok\r\n"
				# 响应头
				response_head = ""
				# 空行
				empty_line = "\r\n"
				# 响应体
				# 图片必须二进制读取
				# 静态资源都在静态的文件夹下面
				with open('./static%s' % file_path, 'rb') as f:
					response_body = f.read()

				# 响应内容
				response_content = response_line.encode("utf-8") + response_head.encode("utf-8") + empty_line.encode(
					"utf-8") + response_body

				# 发送响应内容
				client.send(response_content)
			except Exception as e:
				print("静态资源打开错误", e)
				# 响应行
				response_line = "http/1.1 404 not found\r\n"
				# 响应头
				response_head = ""
				# 空行
				empty_line = "\r\n"
				# 响应体
				# 图片必须二进制读取
				response_body = "not image is find!"

				# 响应内容
				response_content = response_line.encode("utf-8") + response_head.encode("utf-8") + empty_line.encode(
					"utf-8") + response_body.encode("utf-8")

				# 发送响应内容
				client.send(response_content)

		# 关闭
		client.close()

	def runserver(self):
		while True:
			client, address = self.tcp_server.accept()
			# 3. 处理客户端的请求
			# 后期有可能会堵塞,那么把他单独放到一个线程中
			threading.Thread(target=self.client_exec, args=(client,)).start()
		# self.client_exec(client)
		# 4.关闭
		self.tcp_server.close()

	def __init__(self):
		# 初始化套接字服务器
		# 1.创建套接字
		self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# 2.绑定端口与复用端口
		self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.tcp_server.bind(("", 8080))
		# 3.被动模式
		self.tcp_server.listen(128)


# 一个函数一个功能
# main是一个入口函数
# 入口函数读起来像书的目录一样
def main():
	"""web服务器"""
	# 0.实例化webserver
	server = WebServer()

	# 1. 循环接收客户端的请求
	server.runserver()


if __name__ == '__main__':
	main()
