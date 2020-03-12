import socket
def main():
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect(("120.24.188.143",9090))
    received_bytes = socket_client.send("放假了!".encode("gbk"))
    data_socket = socket_client.recv(1024)
    print("接收的信息:",data_socket.decode("utf-8"))
    socket_client.close()
if __name__ == '__main__':
    main()
