class Node(object):
    """docstring for Node"""
    def __init__(self,value,p=0,n=0):
        self.prior = p
        self.data = value
        self.next = n

class DoubleLinkList(object):
    """docstring for SqList"""
    def __init__(self):
        self.head = 0

    def Error(self,s):
        print(s)
        #sys.exit(0)

    def init(self,data):
        self.head = Node(data[0])
        cur = self.head
        for i in data[1:]:
            node = Node(i)
            cur.next = node
            node.prior = cur
            cur = cur.next
        cur.next = self.head
        self.head.prior = cur

    def getLength(self):
        if self.head == 0:
            return 0
        cur = self.head
        length = 0
        while cur.next != self.head:
            length = length + 1
            cur = cur.next
        length = length + 1
        return length

    def clear(self):
        cur = self.head
        while cur.next != self.head:
            q = cur
            cur = cur.next
            del q
        del cur
        self.head = 0

    def isEmpty(self):
        if self.head == 0:
            return True
        else:
            return False

    def traverseGenerator(self):
        if self.head == 0:
            return False
        cur = self.head
        while cur.next != self.head:
            yield cur.data
            cur = cur.next
        yield cur.data

    def traverse(self):
        for g in self.traverseGenerator():
            print(g)

    def getItem(self,index):
        if self.isEmpty():
            self.Error('Linklist is empty')
            return False
        if index > self.getLength() or index < 1:
            self.Error('Index Error')
            return False
        j = 1
        cur = self.head
        while cur.next != self.head and j < index:
            cur = cur.next
            j+=1
        if j == index:
            return cur
        else:
            self.Error('target is not exist')
            return False

    def setItem(self,elem,index):
        if index == 1:
            q = Node(elem,self.head.prior,self.head)
            self.head.prior.next = q
            self.head.prior = q
            self.head = q
            return True
        if index == self.getLength()+1:
            q = Node(elem,self.head.prior,self.head)
            self.head.prior.next = q
            self.head.prior = q
            return True
        cur = self.getItem(index)
        if not cur:
            self.Error("Index Error")
            return False
        node = Node(elem,cur.prior,cur)
        cur.prior.next = node
        cur.prior = node

    def deleteByIndex(self,index):
        """ list.pop(n) """
        if index == 1:
            self.head.prior.next = self.head.next
            self.head.next.prior = self.head.prior
            self.head = self.head.next
            return True
        cur = self.getItem(index)
        if not cur:
            self.Error("Index Error")
            return False
        cur.next.prior = cur.prior
        cur.prior.next = cur.next
        del cur

    def locateElem(self,elem):
        cur = self.head
        j = 1 
        while cur.next != self.head:
            if cur.data == elem:
                return j
            j = j + 1
            cur = cur.next
        if cur.data == elem:
            return j
        return 0

    def deleteByElem(self,elem):
        index = self.locateElem(elem)
        return self.deleteListByIndex(index)

    def append(self,elem):
        cur = Node(elem)
        if self.head == 0:
            self.head = cur
        else:
            p = self.head
            while p.next != self.head:
                p = p.next
            cur.next = p.next
            cur.prior = p
            p.next.prior = cur
            p.next = cur

    def merge(self,anotherlist):
        p = anotherlist.head
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        p.prior.next = self.head
        self.head.prior = p.prior
        cur.next = p
        p.prior = cur



if __name__ == '__main__':
    arr = ["a","b","c","d","e"]
    print("****************************************************************")
    dl = DoubleLinkList()
    dl.init(arr)
    # dl.append("k")
    # dl.traverse()
    # print("****************************************************************")
    # dl.setItem("OK",1)
    # dl.traverse()
    # print("****************************************************************")
    # dl.deleteByIndex(7)
    # dl.traverse()
    # print("****************************************************************")
    # print(dl.locateElem("c"))
    # dl.append("k")
    # dl.traverse()
    #print(dl.getItem(1).data)
    arrnum = [1,2,3]
    dln=DoubleLinkList()
    dln.init(arrnum)
    dl.merge(dln)
    dl.traverse()
    print(dl.getLength())