class Math(object):
    def __init__(self):
        self.__pi = 3.1415926
        self.__int = 19

    @property
    def get_pi(self):
        return self.__pi

    @property
    def get_int(self):
        return self.__int

math = Math()
print(math.get_pi)
print(math.get_int)