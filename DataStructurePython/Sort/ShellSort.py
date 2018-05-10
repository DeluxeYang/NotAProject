#!/usr/bin/env python

import random

def ShellSort(L):#希尔排序是对简单插入排序的改进，插排在记录个数少和基本有序时效率比较高
    mid = len(L)//2#按1/2,1/4,1/8分割若干子序列，分别排序，再合起来排序
    while mid != 0:
        L = ShellInsert(L,mid)
        print(L)
        mid = int(mid/2)
    return L

def ShellInsert(L, mid):
    i = mid
    while i < len(L):
        if L[i] < L[i-mid]:
            temp = L[i]
            j = i-mid
            while j >= 0 and temp < L[j]:
                L[j+mid] = L[j]
                j -= mid
            L[j+mid] = temp
        i += 1
    return L



if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    L = [10,9,8,7,6,5,4,3,2,1]
    print(ShellSort(L))