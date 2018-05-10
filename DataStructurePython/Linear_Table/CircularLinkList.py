import sys
class Node(object):
    """docstring for Node"""
    def __init__(self, value,p=0):
        self.data = value
        self.next = p

class CircularLinkList(object):
    """docstring for SqList"""
    def __init__(self):
        self.head = 0

    def init(self,data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        p.next = self.head

    def Error(self,s):
        print(s)
        sys.exit(0)

    def traverseGenerator(self):
        post = self.head
        p = post.next
        while p != self.head and post.next != self.head:
            yield post.data
            post = p
            p = p.next
        yield post.data

    def traverse(self):
        for g in self.traverseGenerator():
            print(g)


if __name__ == '__main__':
    arr = ["a","b","c","d","e"]
    linklist = CircularLinkList()
    #linklist.setItem("sadadsa",4)
    linklist.init(arr)
    linklist.traverse()
    print("********************************")
    #arrnum = [1,2,3]
    #linklistnum = LinkList()
    #linklistnum.init(arrnum)
    #linklist.merge(linklistnum)
    #linklist.traverse()
