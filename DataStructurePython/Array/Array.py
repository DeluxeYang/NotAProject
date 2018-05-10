class Array(object):
    """docstring for Array"""
    def __init__(self, m, n):
        self.base = [0] * ( m * n )
        self.m = m
        self.n = n

    def _error(self,s):
        print(s)

    def destroy(self):
        del self.base
        self.m, self.n = 0, 0

    def get(self, i, j):
        if i >= 0 and i <self.m and j >= 0 and j < self.n:
            return self.base[self.n * i + j]
        else:
            return self._error(" Suffix Error ")

    def set(self, elem, i, j):
        if i >= 0 and i <self.m and j >= 0 and j < self.n:
            self.base[self.n * i + j] = elem
            return True
        else:
            return self._error(" Suffix Error ")


if __name__ == '__main__':
    T = Array(4,3)
    T.set("0.0",0,0)
    T.set("1.0",1,0)
    T.set("2.0",2,0)
    T.set("3.0",3,0)
    T.set("1.1",1,1)
    T.set("0.0",0,0)
    T.set("0.0",0,0)
    print(T.base)