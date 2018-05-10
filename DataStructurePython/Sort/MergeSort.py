#!/usr/bin/env python

import random

def MergeSort(L,low,high):
    if low < high:
        mid = (low+high)//2
        MergeSort(L,low,mid)
        MergeSort(L,mid+1,high)
        Merge(L,low,mid,high)

def Merge(L,low,mid,high):
    i = low
    j = mid+1
    p = 0
    t = []
    for o in range(len(L)):
        t.append(0)
    while i <= mid and j <= high:
        if L[i] <= L[j]:
            t[p] = L[i]
            p += 1
            i += 1
        else:
            t[p] = L[j]
            p += 1
            j += 1
    while i <= mid:
        t[p] = L[i]
        p += 1
        i += 1
    while j <= high:
        t[p] = L[j]
        p += 1
        j += 1
    p = 0
    for u in range(low,high+1,1):
        L[u] = t[p]
        p += 1


if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    #L = [10,9,8,7,6,5,4,3,2,1]

    MergeSort(L,0,len(L)-1)
    print(L)