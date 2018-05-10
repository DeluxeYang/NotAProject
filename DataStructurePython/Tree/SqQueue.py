#!/usr/bin/env python
"""This script parse the content of a xml file"""


class SqQueue(object):
    """docstring for SqList"""
    def __init__(self, size):
        self.queue = [0] * size
        self.size = size
        self.front = 0
        self.rear = 0

    def _error(self, string):
        ''' Error '''
        print(string)

    def get_length(self):
        ''' get length'''
        return (self.rear-self.front+self.size)%self.size

    def get_len(self):
        ''' get length'''
        return len(self.queue)

    def get_head(self):
        ''' getHead '''
        if self.front == self.rear:
            self._error("Queue Empty")
            return False
        return self.queue[self.front]

    def en_queue(self, elem):
        ''' enQueue '''
        if (self.rear+1)%self.size == self.front:
            self._error("Queue Overflow")
            return False
        self.queue[self.rear] = elem
        self.rear = (self.rear+1)%self.size

    def de_queue(self):
        ''' de queue'''
        if self.front == self.rear:
            self._error("Queue Empty")
            return False
        temp = self.queue[self.front]
        self.front = (self.front+1)%self.size
        return temp


if __name__ == '__main__':
    Q_TEST = SqQueue(100)
    print(Q_TEST.get_length())

    Q_TEST.en_queue("a")
    print(Q_TEST.get_length())
    Q_TEST.en_queue("b")
    print(Q_TEST.get_length())
    Q_TEST.en_queue("c")
    print(Q_TEST.get_length())
    print(Q_TEST.de_queue())
    print(Q_TEST.get_length())
    print(Q_TEST.de_queue())
    print(Q_TEST.get_length())
    