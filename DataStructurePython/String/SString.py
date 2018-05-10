
class SString(object):
    """docstring for SString"""
    def __init__(self, size):
        self.string = [0] * (size+1) 
        self.size = size

    def assign(self,chars):
        chars_len = len(chars)
        if not chars_len:
            self.string[0] = 0
        else:
            j,k = 0,1
            if chars_len > self.size:
                while k <= self.size:
                    self.string[k] = chars[j]
                    k += 1
                    j += 1
                self.string[0] = self.size
            else:
                while k <= chars_len:
                    self.string[k] = chars[j]
                    k += 1
                    j += 1
                self.string[0] = chars_len

    def compare(self,SString):
        loop = min(self.string[0],SString.string[0])
        i = 1
        while i <= loop:
            if self.string[i] != SString.string[i]:
                return ord(self.string[i]) - ord(SString.string[i])
            i += 1
        return self.string[0] - SString.string[0]

    def concat(self,SString):
        if self.string[0] + SString.string[0] <= self.size:
            j = 1
            k = self.string[0] + 1
            while j <= SString.string[0] :
                self.string[k] = SString.string[j]
                k += 1
                j += 1
            self.string[0] = self.string[0] + SString.string[0]
        elif self.string[0] < self.size:
            j = 1
            k = self.string[0] + 1
            while k <= self.size:
                self.string[k] = SString.string[j]
                k += 1
                j += 1
            self.string[0] = self.size

    def copy(self):
        temp = SString(self.size)
        temp.concat(self)
        return temp

    def sub_string(self,index_1=1,index_2=-1):
        if index_2 < 0 or index_2 > self.string[0]+1:
            index_2 = self.string[0]+1
        if index_1 < 0 or index_1 > self.string[0]+1:
            index_1 = 1
        if index_1 > index_2:
            index_2 = index_1+1
        temp = SString(self.size)
        i = 1
        while i <= index_2 - index_1:
            temp.string[i] = self.string[index_1+i-1]
            i += 1
        temp.string[0] = index_2 - index_1
        return temp

    def traverse_generator(self):
        i = 1
        while i <= self.string[0]:
            yield self.string[i]
            i += 1

    def traverse(self):
        for g in self.traverse_generator():
            print(g, end='')
        print("")
            
    def reverse(self):
        s = ''
        i = 0
        for g in self.traverse_generator():
            s += str(g)
        return s


if __name__ == '__main__':
    S_TEST = SString(10)
    S_TEST.assign("abcde")
    # S_TEST2 = S_TEST.copy()
    # S_TEST1 = SString(10)
    # S_TEST1.assign("123")
    # S_TEST.concat(S_TEST1)
    # print(S_TEST.string)
    # print(S_TEST2.string)
    S_TEST1 = S_TEST.sub_string(2,5)
    #print(S_TEST1.reverse())
    S_TEST1.traverse()