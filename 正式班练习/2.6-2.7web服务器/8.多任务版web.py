import socket
import threading


class WebServer(object):
    def __init__(self):
        self.socket_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
        self.socket_server.bind(("",9090))
        self.socket_server.listen(100)

    def run_server(self):
        while True:
            client,address = self.socket_server.accept()
            threading.Thread(target=self.client_exec,args=(client,)).start()

        self.socket_server.close()



    def client_exec(self,client):
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

        print("接收的资源路径:", file_path)


        response_line = 'http://1.1 200ok\r\n'
        response_head = ""
        response_empty = '\r\n'
        if file_path == "/index.html":
            response_body = "hello web!".encode('utf-8')


        elif file_path == "/login.html":
            with open("./post.html",'rb') as f:
                content = f.read()
            response_body = content


        elif file_path.endswith(".jpg"):
            try:
                with open("." + file_path,'rb') as f:
                    content = f.read()
                response_body = content

            except Exception as e:
                print('异常:',e)
                response_body = 'you are wrong!'.encode('utf-8')

        else:
            response_line = "http:/1/1 404 not found\r\n"
            response_body = "no page is shown!".encode('utf-8')

        response_data = response_line.encode('utf-8') + response_head.encode('utf-8') + response_empty.encode('utf-8') + response_body
        client.send(response_data)

        client.close()

def main():
    server = WebServer()
    server.run_server()

if __name__ == '__main__':
    main()