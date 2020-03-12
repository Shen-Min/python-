import socket


def client_exec(clinet):
    data_recv = clinet.recv(1024)
    if data_recv:
        decode_data = data_recv.decode("gbk")
        split_list_data = decode_data.split(" ")
        try:
            file_path= split_list_data[1]
            print("接收的资源路径:",file_path)
            if file_path == "/":
                file_path = "/index.html"
        except Exception as e:
            print("异常:",e)
            clinet.close()
            return

    else:
        clinet.close()
        return

    if file_path == "/index.html":
        response_line = "http:/1/1 200ok\r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "hello everyone!"
        response_data = response_line + response_head + response_empty + response_body
        clinet.send(response_data.encode("utf-8"))

    elif file_path == "/center.html":
        response_line = "http:/1/1 200ok\r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "hello web!"
        response_data = response_line + response_head + response_empty + response_body
        clinet.send(response_data.encode("utf-8"))

    elif file_path == "/login.html":
        response_line = "http:/1/1 200ok \r\n"
        response_head = ""
        response_empty = "\r\n"
        with open("./post.html",encoding='utf-8') as f:
           content = f.read()
        response_body = content
        response_data = response_line + response_head + response_empty + response_body
        clinet.send(response_data.encode("utf-8"))

    else:
        response_line = "http:/1/1 404 not find\r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "not page is find"
        response_data = response_line + response_head + response_empty + response_body
        clinet.send(response_data.encode('utf-8'))
    clinet.close()

def main():
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_server.bind(("",9090))
    socket_server.listen(120)
    while True:
        clinet,address = socket_server.accept()
        client_exec(clinet)
    socket_server.close()

if __name__ == '__main__':
    main()

