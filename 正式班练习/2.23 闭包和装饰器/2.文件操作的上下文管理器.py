class Open_file(object):
    def __init__(self,path):
        self.f = open(path)

    def __enter__(self):
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.f.close()

with Open_file("a.txt") as f:
    countent = f.read()
print(countent)