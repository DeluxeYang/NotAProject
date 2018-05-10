class SqStack(object):
    """docstring for SqList"""
    def __init__(self,size):
        self.stack = [0] * size
        self.size = size
        self.top = -1

    def Error(self,s):
        print(s)

    def destroy(self):
        del self.stack
        self.top = -1

    def clear(self):
        self.stack = []
        self.top = -1

    def push(self,elem):
        if self.top == self.size - 1:
            self.Error("Stack Overflow")
            return False
        #self.stack.append(elem)
        self.top = self.top + 1
        self.stack[self.top] = elem

    def getLength(self):
        return self.top + 1

    def getLen(self):
        return len(self.stack)

    def getSize(self):
        return self.size

    def pop(self):
        if self.top == -1:
            self.Error("Stack Empty")
            return False
        e = self.stack[self.top]
        del self.stack[self.top]
        self.top = self.top - 1
        return e

    def generator(self):
        for e in self.stack:
            yield e

    def traverse(self):
        for g in self.generator():
            print(g)

    def getTop(self):
        if self.top == -1:
            self.Error("Stack Empty")
            return False
        return self.stack[self.top]


if __name__ == '__main__':
    s = SqStack(100)
    s.push("1")
    s.push("1")
    s.push("1")
    #s.traverse()
    print(s.getLength())
    print("***************************************************************************")
    s.pop()
    #s.traverse()
    print(s.getLength())