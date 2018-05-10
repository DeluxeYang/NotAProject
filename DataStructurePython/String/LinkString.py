class Node(object):
    """docstring for Node"""
    def __init__(self, value,p=0):
        self.letter = value
        self.next = p


class LinkString(object):
    """docstring for SString"""
    def __init__(self):
        self.ch = 0
        self.length = 0

    def assign(self,chars):
        chars_len = len(chars)
        if self.ch != 0:
            cur = self.ch
            while cur != 0:
                p = cur.next
                del cur
                cur = p
            self.ch = 0
            self.length = 0
        if not chars_len:
            self.ch = 0
            self.length = 0
        else:
            k = chars_len-1
            cur = 0
            while k > 0:
                node = Node(chars[k],cur)
                k -= 1
                cur = node
            self.ch = Node(chars[0],cur)
            self.length = chars_len

    def compare(self, S):
        cur_1 = self.ch
        cur_2 = S.ch
        while cur_1 != 0 and cur_2 != 0:
            if cur_1.letter != cur_2.letter :
                return ord(cur_1.letter) - ord(cur_2.letter)
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        return self.length - S.length

    def concat(self,S):
        cur = self.ch
        while cur.next != 0:
            cur = cur.next
        cur.next = S.copy().ch
        self.length += S.length

    def copy(self):
        temp = LinkString()
        cur = temp.ch
        temp.length = self.length
        for g in self.traverse_generator_reverse():
            node = Node(g.letter,cur)
            cur = node
        temp.ch = node
        return temp

    def copy_reverse(self):
        temp = LinkString()
        cur = temp.ch
        temp.length = self.length
        for g in self.traverse_generator():
            node = Node(g.letter,cur)
            cur = node
        temp.ch = node
        return temp

    def sub_string(self,index_1=1,index_2=-1):
        if index_2 < 0 or index_2 > self.length+1:
            index_2 = self.length+1
        if index_1 < 1:
            index_1 = 1
        if index_2 < index_1:
            return False
        temp = LinkString()
        i = index_2 - 1
        cur = 0
        temp_list = self.traverse_list()
        while i >= index_1:
            node = Node(temp_list[i-1].letter,cur)
            cur = node
            i -= 1
        temp.ch = node
        temp.length = index_2-index_1
        return temp

    def traverse_list(self):
        temp_list = []
        cur = self.ch
        while cur != 0:
            temp_list.append(cur)
            cur = cur.next
        return temp_list 

    def traverse_generator_reverse(self):
        temp_list = self.traverse_list()
        for i in temp_list[::-1]:
            yield i

    def traverse_reverse(self):
        for g in self.traverse_generator_reverse():
            print(g.letter, end='')
        print("")

    def traverse_generator(self):
        cur = self.ch
        while cur != 0:
            yield cur
            cur = cur.next

    def traverse(self):
        for g in self.traverse_generator():
            print(g.letter, end='')
        print("")
            
    def str(self):
        s = ''
        i = 0
        for g in self.traverse_generator():
            s += str(g)
        return s


if __name__ == '__main__':
    S_TEST = LinkString()
    S_TEST.assign("abcde")
    S_TEST1 = LinkString()
    S_TEST1.assign("123")
    S_TEST.concat(S_TEST1)
    S_TEST2 = S_TEST.sub_string(4,9)
    S_TEST2.traverse()
    S_TEST.traverse()