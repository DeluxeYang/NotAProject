#!/usr/bin/env python

import random

def BubbleSort(L):#冒泡排序
    tag, bound = 0, 0
    while tag == 0:
        tag = 1#tag=1
        for i in range(len(L)-1,bound,-1):#从最后一个元素开始
            if L[i-1] > L[i]:#如果前一个大于后一个
                L[i],L[i-1] = L[i-1],L[i]#则交换
                tag = 0#tag=0，意味着还应该继续循环
        bound += 1#已排序部分+1
    return L



if __name__ == '__main__':
    L = range(0,100)
    L = random.sample(L, 10)

    #L = [10,9,8,7,6,5,4,3,2,1]
    print(BubbleSort(L))
    print(L)