#!/usr/bin/env python
"""This script parse the content of a xml file"""
class SqList(object):
    """docstring for SqList"""
    def __init__(self, size):
        self.list = [0] * size
        self.size = size
        self.length = 0

    def _error(self,s):
        print(s)

    def init_by_arr(self,arr):
        i = 0
        length = len(arr)
        while i < length:
            self.list[i] = arr[i]
            i += 1
        self.length = length

    def get_list_generator(self):
        for i in range(self.length):
            yield self.list[i]

    def traverse(self):
        for g in self.get_list_generator():
            print(g)

    def get_length(self):
        return self.length

    def clear_list(self):
        self.list = [0] * self.size
        self.length = 0

    def destroy_list(self):
        del self.list
        self.length = 0

    def get_elem_by_index(self,index):
        if index < 1 or index > self.length:
            self._error("index error")
        return self.list[index-1]

    def append(self, elem):
        self.list[self.length]=elem
        self.length += 1

    def locate(self,elem):
        i = 1
        for n in range(self.length):
            if elem == self.list[n]:
                return i
            i = i + 1
        return 0
    
    def insert(self,elem,index):
        """ list.insert(n,elem) """
        if index < 1 or index > self.length+1:
            self._error("index error")
        if self.length >= self.size:
            self._error("list overflow")
        i = self.length
        while i >= index:
            self.list[i] = self.list[i-1]
            i -= 1
        self.list[i] = elem
        self.length += 1
    
    def delete_by_index(self,index):
        """ list.pop(n) """
        if index < 1 or index > self.length:
            self._error("index error")
            return False
        temp = self.list[index-1]
        i = index-1
        while i < self.length-1:
            self.list[i] = self.list[i+1]
            i = i + 1
        self.list[-1] = 0
        self.length = self.length - 1
        return temp

    def delete_by_elem(self,elem):
        index = self.locate(elem)
        return self.delete_by_index(index)

    def merge_list(self,anotherlist):
        for e in anotherlist.list:
            self.append(e)
        self.length = self.length + anotherlist.get_length()



if __name__ == '__main__':
    # arr = ["a","b","c","d","e"]
    # S_TEST = SqList(100)
    # S_TEST.init_by_arr(arr)
    # print(S_TEST.get_length())
    # S_TEST.insert("2",6)
    # S_TEST.delete_by_index(4)
    # S_TEST.traverse()