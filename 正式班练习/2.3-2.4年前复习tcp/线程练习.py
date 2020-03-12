import threading
import time

lock = threading.Lock()

num = 0


def sum_num1():
    lock.acquire()
    global num
    for i in range(10000):
        num += 1
    print("sum_num1是:", num)
    lock.release()


def sum_num2():
    lock.acquire()
    global num
    for i in range(10000):
        num += 1
    print("sum_num2是:", num)
    lock.release()


def main():
    threading.Thread(target=sum_num1).start()
    threading.Thread(target=sum_num2).start()
    time.sleep(1)
    print("最终结果:", num)



if __name__ == '__main__':
    main()
