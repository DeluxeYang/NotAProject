
class Node(object):
    """docstring for Node"""
    def __init__(self, value,p=0):
        self.data = value
        self.next = p

class LinkList(object):
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

    def Error(self,s):
        print(s)
        #sys.exit(0)

    def getLength(self):
        p = self.head
        length = 0
        while p != 0:
            length = length + 1
            p = p.next
        return length

    def isEmpty(self):
        if self.getLength() == 0:
            return True
        else:
            return False

    def clear(self):
        p = self.head
        while p != 0:
            q = p
            p = p.next
            del q
        self.head = 0

    def traverseGenerator(self):
        p = self.head
        while p != 0:
            yield p.data
            p = p.next

    def traverse(self):
        for g in self.traverseGenerator():
            print(g)

    def getItem(self,index):
        if self.isEmpty():
            self.Error('Linklist is empty')
            return False
        j = 1
        p = self.head
        while p.next!=0 and j <index:
            p = p.next
            j+=1
        if j ==index:
            return p.data
        else:
            self.Error('target is not exist')
            return False

    def setItem(self,elem,index):
        if self.isEmpty():
            self.Error('Linklist is empty')
            return False
        if index < 1 or index > self.getLength():
            self.Error('Index Error')
            return False
        if index == 1:
            q = Node(elem,self.head)
            self.head = q
            return
        p = self.head
        post = self.head
        j = 1
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j = j + 1
        if index == j:
            q = Node(elem,p)
            post.next = q

    def deleteByIndex(self,index):
        """ list.pop(n) """
        if self.isEmpty():
            self.Error('Linklist is empty')
            return False
        if index < 1 or index > self.getLength():
            self.Error('Index Error')
            return False
        if index == 1:
            temp = self.head.data
            self.head = self.head.next
            return temp
        p = self.head
        post = self.head
        j = 1
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j = j + 1
        if index == j:
            post.next = p.next
            return p.data

    def locateElem(self,elem):
        p = self.head
        j = 1 
        while p != 0:
            if p.data == elem:
                return j
            j = j + 1
            p = p.next
        return 0

    def deleteByElem(self,elem):
        index = self.locateElem(elem)
        return self.deleteListByIndex(index)

    def append(self,elem):
        q = Node(elem)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def initReverse(self, data):
        self.head = Node(data[-1])
        for i in data[:-1]:
            p = Node(i)
            p.next = self.head.next
            self.head.next = p

    def merge(self,anotherlist):
        p = anotherlist.head
        while p != 0:
            self.append(p.data)
            p = p.next


if __name__ == '__main__':
    arr = ["a","b","c","d","e"]
    linklist = LinkList()
    #linklist.setItem("sadadsa",4)
    linklist.init(arr)
    linklist.traverse()
    # print("********************************")
    # arrnum = [1,2,3]
    # linklistnum = LinkList()
    # linklistnum.init(arrnum)
    # linklist.merge(linklistnum)
    # linklist.traverse()
    print(linklist.locateElem("c"))