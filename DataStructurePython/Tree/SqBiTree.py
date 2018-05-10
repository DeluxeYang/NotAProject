class SqBiTree(object):
    """docstring for """
    def __init__(self,size):
        self.tree = [0] * size
        self.size = size

    def init_by_arr(self,arr):
        i = 1
        self.tree[0] = len(arr)
        while i <= self.tree[0]:
            self.tree[i] = arr[i-1]
            i += 1

    def PreOrderBiTree(self):
        i = 1
        while i <= self.tree[0]:
            if i == 1:
                j = 1
            elif j * 2 <= self.tree[0]:
                j = 2 * j
            elif j % 2 == 0 and j < self.tree[0]:
                j += 1
            elif j > 1:
                while int(j/2)%2!=0:
                    j = int(j/2)
                j = int(j / 2 + 1)
            print(self.tree[j])
            i += 1
            

if __name__ == '__main__':
    t = SqBiTree(16)
    t.init_by_arr(['A','B','C','D','E','F','G'])

    print(t.tree)
    t.PreOrderBiTree()