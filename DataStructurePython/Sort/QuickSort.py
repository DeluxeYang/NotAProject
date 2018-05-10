#!/usr/bin/env python

import random

def QuickSort(L, low, high):
    if low < high:
        pivotpos = Partition(L,low,high)#一次划分
        QuickSort(L,low,pivotpos-1)#递归左半部分
        QuickSort(L,pivotpos+1,high)#递归右半部分
    return L

def Partition(L, low, high):#一次划分
    pivotkey = L[low]#以low为轴
    while low < high:
        while low < high and L[high] >= pivotkey:#如果high比pivot大，则high向左移动
            high -= 1
        L[low],L[high] = L[high],L[low]#直到high比pivot小，则high low 交换
        while low < high and L[low] <= pivotkey:#如果low比pivot小，则low向右移动
            low += 1
        L[low],L[high] = L[high],L[low]#直到low比pivot大，则high low交换
    L[low] = pivotkey
    return low


if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    L = [10,9,8,7,6,5,4,3,2,1]
    print(QuickSort(L,0,len(L)-1))
    print(L)