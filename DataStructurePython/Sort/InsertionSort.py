#!/usr/bin/env python

import random

def InsertSort(L):#插入排序，选择下一个待排序的数，插入到左边有序位置
    for i in range(1,len(L)):
        if L[i] < L[i-1]:
            temp = L[i]
            j = i-1
            while temp < L[j] and j >= 0:
                L[j+1] = L[j]
                j -= 1
            L[j+1] = temp
    return L


if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    #L = [5,6,8,3,2,4,9,1,6,7,65,6]
    print(InsertionSort(L))