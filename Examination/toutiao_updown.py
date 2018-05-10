#!/usr/bin/env python  
# coding=utf-8  
# 输入[ 或者 ]，然后绘图输出，要求外层套住里层
import math

LL = {}

L = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]
n = len(L)
if n != "":
    flag = 1#1为上升
    last_num = L[0]
    temp = {0:last_num}
    for i in range(1,n):
        if last_num < L[i]:
            if flag == 0:#在下降中，后一个又比前一个大了
                LL[i]= temp
                temp = {i-1:last_num}#重置
                flag = 1
        if last_num > L[i]:
            flag = 0#0为下降
        temp[i]=L[i]
        last_num = L[i]
    if flag == 0:
        LL[i]= temp
    max_len = 0
    index = 0
    print(LL)
    for k in LL:
        if max_len < len(LL[k]):
            max_len = len(LL[k])
            index = k
    min_index = n
    max_index = 0    
    for j in LL[index]:
        if min_index > j:
            min_index = j
        if max_index < j:
            max_index = j
    print("%d %d"%(min_index,max_index))