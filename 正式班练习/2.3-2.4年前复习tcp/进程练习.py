import multiprocessing
import time


def dance(name,age):
    while True:
        print("跳舞",name,age)
        time.sleep(1)

def song(name,age):
    while True:
        print("唱歌",name,age)
        time.sleep(1)

def main():
    process_dance = multiprocessing.Process(target=dance,args=("小班",18))
    process_dance.start()

    process_song = multiprocessing.Process(target=song,kwargs={"name":"中班","age":19})
    process_song.start()
    time.sleep(3)

    process_dance.terminate()
    process_song.terminate()


if __name__ == '__main__':
    main()