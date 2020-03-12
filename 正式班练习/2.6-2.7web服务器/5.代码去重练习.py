import socket


def client_exec(client):
    data_recv = client.recv(1024)
    if data_recv:
        data_decode = data_recv.decode('utf-8')
        split_list_data = data_decode.split(" ")
        try:
            file_path = split_list_data[1]
            if file_path == "/":
                file_path = "/index.html"

        except Exception as e:
            print("异常:",e)
            client.close()
            return

    else:
        client.close()
        return

    response_line = "http:/1/1 200 ok\r\n"
    response_head = ""
    response_empty = "\r\n"

    if file_path == "/index.html":

        response_body = "hello web!".encode('utf-8')


    elif file_path == "/login.html":

        with open("./post.html",'rb') as f:
            content = f.read()
        response_body = content

    elif file_path == "/jd.html":

        with open("./jdg.html",'rb') as f:
            content = f.read()
        response_body = content

    else:
        print(file_path)
        try:
            with open("." + file_path,'rb') as f:
                content = f.read()
            response_body = content
        except:
            print("error read file")
            response_body = b''



    response_data = response_line.encode('utf-8') + response_head.encode('utf-8') + response_empty.encode('utf-8') + response_body
    client.send(response_data)

    client.close()

def main():
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_server.bind(("",9090))
    socket_server.listen(110)
    while True:
        client,address = socket_server.accept()
        client_exec(client)

    socket_server.close()

if __name__ == '__main__':
    main()