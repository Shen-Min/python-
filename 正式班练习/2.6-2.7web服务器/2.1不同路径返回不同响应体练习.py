import socket

def client_exec(client):
    recv_data = client.recv(1024)
    if recv_data:
        data_decode = recv_data.decode("gbk")
        split_list_code = data_decode.split(" ")
        try:
            file_path = split_list_code[1]
            print("得到的资源路径:",file_path)
            if file_path == "/":
                file_path = "/index.html"

        except Exception as e:
            print("异常",e)
            client.close()
            return
    else:
        client.close()
        return

    if file_path == "/index.html":
        response_line = "http:/1/1 200 ok \r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "index page is show!name:huahua"
        response_data = response_line + response_head + response_empty + response_body
        client.send(response_data.encode("utf-8"))

    elif file_path == "/center.html":
        response_line = "http:/1/1 200 ok \r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "center page is show C!"
        response_data = response_line + response_head + response_empty + response_body
        client.send(response_data.encode("utf-8"))

    else:
        response_line = "http:/1/1 404 not find\r\n"
        response_head = ""
        response_empty = "\r\n"
        response_body = "not page is show!"
        response_data = response_line + response_head + response_empty + response_body
        client.send(response_data.encode("utf-8"))

    client.close()


def main():
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_server.bind(("",3030))
    socket_server.listen(120)
    while True:
        client,address = socket_server.accept()
        client_exec(client)


if __name__ == '__main__':
    main()