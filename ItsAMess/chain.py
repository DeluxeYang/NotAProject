class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        print("__getattr__")
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    def __call__(self, path):
        print("__call__")
        return Chain('%s/%s' % (self._path, path))

    __repr__ = __str__

print(Chain("api").users("David"))
