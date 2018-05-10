#!/usr/bin/env python
"""This script parse the content of a xml file"""
class Node(object):
    """docstring for Node"""
    def __init__(self, value,p=0):
        self.data = value
        self.next = p

class LinkQueue(object):
    """docstring for SqList"""
    def __init__(self):
        self.front = 0
        self.rear = 0

    def _error(self, string):
        ''' Error '''
        print(string)

    def en_queue(self,elem):
        ''' en queue '''
        node = Node(elem)
        if self.front == 0:
            self.front = node
            self.rear = node
            return True
        self.rear.next = node
        self.rear = node
        return True

    def de_queue(self):
        ''' de queue '''
        if self.front == 0:
            self._error("Queue Empty")
            return False
        p = self.front
        temp = p.data
        self.front = self.front.next
        if self.rear == p:
            self.rear = self.front
        del p
        return temp

    def destroy_queue(self):
        while self.front:
            self.rear = self.front.next
            del self.front
            self.front = self.rear

    def get_length(self):
        ''' get length'''
        cur = self.front
        length = 0
        while cur != 0:
            length += 1
            cur = cur.next
        return length

    def get_head(self):
        ''' get queue '''
        if self.front == 0:
            self._error("Queue Empty")
            return False
        return self.front.data


if __name__ == '__main__':
    Q_TEST = LinkQueue()
    #print(Q_TEST.get_length())
    Q_TEST.en_queue("a")
    #print(Q_TEST.get_length())
    Q_TEST.en_queue("b")
    #print(Q_TEST.get_length())
    Q_TEST.en_queue("c")
    # print(Q_TEST.get_length())
    # print(Q_TEST.de_queue())
    # print(Q_TEST.get_length())
    # print(Q_TEST.de_queue())
    # print(Q_TEST.get_length())
    # print(Q_TEST.de_queue())
    # print(Q_TEST.get_length())
    # print(Q_TEST.de_queue())
    # print(Q_TEST.get_length())
    print(Q_TEST.get_head())
    print(Q_TEST.get_length())