def out_func(num1):
    def inner_func(num2):
        result = num1 + num2
        print("结果:",result)
    return inner_func

f = out_func(1)
f(2)
f(3)

