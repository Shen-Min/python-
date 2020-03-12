from flask import Flask

app = Flask(__name__)  # 初始化


# 定义一个请求处理的地址

@app.route('/index.html')
def index():
	return "index page is show!"


@app.route('/center.html')
def center():
	return "center page is show!"


@app.route('/regedit.html')
def regedit():
	return "regedit page is show!"


# 运行
if __name__ == '__main__':
	app.run()
