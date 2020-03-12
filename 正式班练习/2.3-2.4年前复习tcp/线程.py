import threading
import time

lock = threading.Lock()

num = 0
def sum_num1():
    print("sum_num1开始")
    lock.acquire()
    global num
    for i in range(10000):
        num += 1
    print("sum_num1结束:",num)
    lock.release()

def sum_num2():
    print("sum_num2开始")
    global num
    for i in range(10000):
        lock.acquire()
        num += 1
        lock.release()
    print("sum_num2结束:",num)

def main():
    threading.Thread(target=sum_num1).start()
    threading.Thread(target=sum_num2).start()
    time.sleep(1)
    print("最终结果:",num)

if __name__ == '__main__':
    main()