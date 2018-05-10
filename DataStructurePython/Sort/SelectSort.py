#!/usr/bin/env python

import random

def SelectSort(L):
    for i in range(0,len(L),1):#简单选择排序，时间复杂度O(n^2)
        k = i
        for j in range(i+1,len(L),1):#从每趟循环中，选择最小的记录
            if L[j] < L[k]:
                k = j
        if i != k:#如果i不是最小的，则i和最小的交换，放到已排序的部分
            L[i],L[k] = L[k],L[i]
    return L


if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    #L = [10,9,8,7,6,5,4,3,2,1]
    SelectSort(L)
    print(L)