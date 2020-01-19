import threading
import time


def dance():
    while True:
        print("跳舞")
        time.sleep(5)

def song():
    while True:
        print("唱歌")
        time.sleep(1)

if __name__ == '__main__':
    thread_dance = threading.Thread(target=dance,daemon=True)
    thread_dance.start()

    threading.Thread(target=song,daemon=True).start()
    time.sleep(3)



