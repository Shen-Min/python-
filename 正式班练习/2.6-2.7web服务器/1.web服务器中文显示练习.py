import socket


def client_exec(client):
    data_recv = client.recv(1024)
    print("接收到的请求:",data_recv.decode("gbk"))
    response_line = "http:/1.1 200 ok \r\n"
    response_head = "content-type:text/html;charset=utf-8\r\n"
    response_empty = "\r\n"
    response_body = "老师好!"
    response_data = response_line + response_head + response_empty +response_body
    client.send(response_data.encode("utf-8"))
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