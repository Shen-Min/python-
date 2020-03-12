import socket


def main():
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_client.connect(("120.24.188.143",9090))
    while True:
        data = input(":")
        socket_client.send(data.encode("utf-8"))
        data = socket_client.recv(1024)
        print("接收的数据:",data.decode("utf-8"))
    socket_client.close()

if __name__ == '__main__':
    main()
