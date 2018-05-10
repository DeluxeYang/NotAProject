#!/usr/bin/env python  
# coding=utf-8  
# 输入[ 或者 ]，然后绘图输出，要求外层套住里层
s = '[[[]]][[]]'


d = {}
max_depth = 0
depth = 0
for i in range(len(s)):
    if s[i] == '[':
        depth += 1
        d[i] = (s[i],depth)
    elif s[i] == ']':
        d[i] = (s[i],depth)
        depth -= 1
    if max_depth < depth:
        max_depth = depth
flag = 0
left_not_pre_print = 1
right_not_pre_print = 1
left_first_print = 1
right_first_print = 1
for i in d:
    if d[i][0] == '[':
        temp1 = ' '*(d[i][1]-1)+'+'+'-'*((max_depth-d[i][1]+1)*2-1)+'+'
        if i+1 in d and d[i+1][0] == '[':
            temp3 = '+'+'-'*((max_depth-d[i+1][1]+1)*2-1)+'+'
            temp2 = ' '*(d[i][1]-1)+'|'+temp3+'|'
            left_not_pre_print = 0
        else:
            temp2 = ' '*(d[i][1]-1)+'|'+' '*((max_depth-d[i][1]+1)*2-1)+'|'
        if left_not_pre_print or left_first_print:
            print(temp1)
            left_first_print = 0
        print(temp2)
        right_not_pre_print = 1
        right_first_print = 1
        flag = 1
    if d[i][0] == ']':
        if flag == 1:
            print()
        temp3 = '-'*((max_depth-d[i][1]+1)*2-1)
        if i+1 in d and d[i+1][0] == ']':
            temp1 = ' '*(d[i+1][1]-1)+'|+'+temp3+'+|'
            right_not_pre_print = 0
        else:
            temp1 = ' '*(d[i][1]-1)+'+'+temp3+'+'
        temp2 = ' '*(d[i][1]-1)+'|'+' '*((max_depth-d[i][1]+1)*2-1)+'|'
        if right_not_pre_print or right_first_print:
            print(temp2)
            right_first_print = 0
        print(temp1)
        left_not_pre_print = 1
        left_first_print = 1
        flag = 0