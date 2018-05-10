class Tree(object):
    """docstring for Tree"""
    def __init__(self, data, level):
        self.data = data
        self.level = level
        self.children = []

    def traverse(self):
        print(self.data)
        for child in self.children:
            child.traverse()

    def add(self, *args):
        for i in args:
            self.children.append(i)


if __name__ == '__main__':
    A = Tree("A",0)
    B = Tree("B",1)
    C = Tree("C",1)
    D = Tree("D",2)
    A.add(B,C)
    B.add(D)
    A.traverse()