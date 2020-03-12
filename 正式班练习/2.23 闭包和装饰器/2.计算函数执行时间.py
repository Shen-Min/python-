import time

def set_fun(args):
    def call_fun():
        start_time = time.time()
        time.sleep(3)
        end_time = time.time()

        print(end_time - start_time)
        args()

    return call_fun

@set_fun
def test():
    print('test')

test()