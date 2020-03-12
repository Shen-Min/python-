#web服务器通讯使用tpc服务器
#1.初始化socket
#2.绑定及复用端口
#3.监听
#4.循环接收客户端
#5.处理客户端请求
#6.关闭

import socket


def client_exec(client):
    data = client.recv(1024)
    print("请求的数据:",data.decode("gbk"))
    response_line = "http:/1/1 200 ok \r\n"
    response_head = ""
    response_empty = "\r\n"
    response_body = "hello world! hello web!"
    response_data = response_line + response_head + response_empty + response_body
    client.send(response_data.encode("utf-8"))
    client.close()


def main():
    socket_sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_sever.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_sever.bind(("",9090))
    socket_sever.listen(120)
    while True:
        client,address = socket_sever.accept()
        client_exec(client)
    socket_sever.close()

if __name__ == '__main__':
    main()