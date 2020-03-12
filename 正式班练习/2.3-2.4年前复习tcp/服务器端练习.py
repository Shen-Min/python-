#1.初始化socket
#2.绑定及复用端口
#3.监听
#4.循环接收客户端请求
#5.处理客户端请求
#6.关闭
import socket

def client_exec(client):
    data_recv = client.recv(1024)
    print("接收到的信息:",data_recv.decode("gbk"))

    client.send("亲,您的请求已收到!".encode("utf-8"))
    client.close()

def main():
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_server.bind(("",8080))
    socket_server.listen(128)
    while True:

        client,address = socket_server.accept()
        client_exec(client)

    socket_server.close()

if __name__ == '__main__':
    main()