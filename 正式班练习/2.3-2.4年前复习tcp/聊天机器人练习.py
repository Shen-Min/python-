import socket
import threading
import time
from datetime import datetime
def client_exec(client):
    while True:
        data = client.recv(1024)
        if data:
            action = data.decode("gbk")
            print(action)
            if action == "1":
                client.send("您的请求已收到一次!".encode("utf-8"))
            elif action == "2":
                client.send("您的请求已收到二次!".encode("utf-8"))
            elif action == "3":
                client.send("您的请求已收到三次!" .encode("utf-8")+ datetime.now().strftime('%H:%M:%S').encode("utf-8"))
            elif action == "4":
                client.send(time.ctime().encode("utf-8"))
            else:
                client.send("请转人工服务".encode("utf-8"))
        else:
            break


    client.close()


def main():
    socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
    socket_server.bind(("",8080))
    socket_server.listen(120)
    while True:
        client,address = socket_server.accept()

        threading.Thread(target=client_exec,args=(client,),daemon=True).start()

    socket_server.close()
if __name__ == '__main__':
    main()