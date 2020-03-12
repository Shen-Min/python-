
def set_fun(func):
    num = 0
    def call_fun(*args,**kwargs):
        nonlocal num
        num += 1
        print('执行的次数:',num)
        return func(*args,**kwargs)

    return call_fun


@set_fun
def test():
    print("test")

test()
test()
test()