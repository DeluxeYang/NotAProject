#!/usr/bin/env python
"""This script parse the content of a xml file"""
import random

def HeapSort(L):#堆排序，大根堆
    for i in range(len(L)//2,-1,-1):#初始建大根堆，从n/2开始调整
        HeapAdjust(L,i,len(L)-1)
    for h in range(len(L)-1,0,-1):
        L[0],L[h] = L[h],L[0]
        HeapAdjust(L,0,h-1)

def HeapAdjust(L,low,high):#
    temp = L[low]
    j = low * 2
    while j <= high:
        if j<high and L[j] < L[j+1]:
            j+=1
        if not temp < L[j]:
            break
        L[low]=L[j]
        low = j
        j = j * 2
    L[low] = temp


if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 11)

    #L = [10,9,8,7,6,5,4,3,2,1]
    HeapSort(L)
    print(L)