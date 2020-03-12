import time
import gevent
from gevent import monkey
monkey.patch_all()

def dance(name,age):
    while True:
        print("跳舞__",name,age)
        time.sleep(1)

def song(name,age):
    while True:
        print("唱歌__",name,age)
        time.sleep(1)


def main():
    spawn1 = gevent.spawn(dance,"小班",18)
    spawn2 = gevent.spawn(song,name="中班",age=19)

    gevent.joinall([spawn1,spawn2])


if __name__ == '__main__':
    main()


