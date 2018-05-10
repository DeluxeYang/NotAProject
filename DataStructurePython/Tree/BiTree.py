import SqQueue
class BiTree(object):
    """docstring for """
    def __init__(self,data,left=0,right=0):
        self.data = data
        self.left = left
        self.right = right

def InOrderBiTree(BT):
    if BT != 0:
        InOrderBiTree(BT.left)
        print(BT.data)
        InOrderBiTree(BT.right)

def init(BT):
    #temp = input("input:")
    temp = Q_TEST.de_queue()
    if temp == '':
        BT = 0
    else:
        BT = BiTree(temp)
        init(BT.left)
        init(BT.right)
