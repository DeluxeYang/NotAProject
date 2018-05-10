class CPoint(object):
    ''''''
    def __init__(self):
        self.child = 0
        self.next = 0

class PCTNode(object):
    """docstring for """
    def __init__(self, data=0, parent=0, firstchild=0):
        self.data = data
        self.parent = parent
        self.firstchild = firstchild

class PCTree(object):
    """docstring for PCTree"""
    def __init__(self):
        self.tnode = []
        self.num = 0

    def initTree(self, data):
        temp = PCTNode(data,-1)
        self.tnode.append(temp)
        self.num += 1

    def add(self, data, parent):
        temp = PCTNode(data,parent)
        

    def traverse(self):
        pass


if __name__ == '__main__':
    pctnode = PCTNode()
    PCT = PCTree()
    PCT.add(pctnode)