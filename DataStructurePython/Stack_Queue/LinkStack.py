
class Node(object):
    """docstring for Node"""
    def __init__(self, value,p=0):
        self.data = value
        self.next = p

class LinkStack(object):
    """docstring for SqList"""
    def __init__(self):
        self.head = 0

    def Error(self,s):
        print(s)

    def push(self,elem):
        if self.head == 0:
            self.head = Node(elem)
            return True
        node = Node(elem,self.head)
        self.head = node
        return True

    def destroy(self):
        cur = self.head
        while cur != 0:
            q = cur
            cur = cur.next
            del cur
        self.head = 0

    def generator(self):
        cur = self.head
        while cur != 0:
            yield cur
            cur = cur.next

    def traverse(self):
        for g in self.generator():
            print(g.data,g.next)

    def pop(self):
        if self.head == 0:
            self.Error("Stack Empty")
            return False
        temp = self.head
        self.head = self.head.next
        return temp

    def getLength(self):
        cur = self.head
        length = 0
        while cur != 0:
            length = length + 1
            cur = cur.next
        return length


if __name__ == '__main__':
    s = LinkStack()
    s.push("1")
    s.push("2")
    s.push("3")
    s.pop()
    s.pop()
    s.traverse()
    print(s.getLength())