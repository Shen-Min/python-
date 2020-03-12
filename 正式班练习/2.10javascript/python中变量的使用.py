a=10
def funtion():
    b=5

    global a
    a += 1
    print(a)
    print(b)

funtion()
print(a)
print(b)