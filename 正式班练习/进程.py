import multiprocessing
import time

def dance():
    while True:
        print("跳舞")
        time.sleep(0.5)

def song():
    while True:
        print("唱歌")
        time.sleep(1)


def main():
    process_dance = multiprocessing.Process(target=dance)
    process_dance.start()

    process_song = multiprocessing.Process(target=song)
    process_song.start()

    time.sleep(6)
    #进程可以手动关闭
    process_dance.terminate()
    process_song.terminate()

if __name__ == '__main__':
    main()
