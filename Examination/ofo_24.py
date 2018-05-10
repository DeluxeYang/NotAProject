"""
算24点游戏大家应该都玩过，每次取出4张牌，使用加减乘除将4个数算出24。
比如8 2 4 6：8*2=16，16*6=96，96/4=24，说明这组牌是能算出24点的。
但是碰到无解的情况，人往往不能很快得出结论，这时就需要借助程序的帮助了。
请实现一个判断给定的牌是否能算出24点的程序，如果有解，输出true，否则输出false。
"""

import itertools

def Check24(data):
    # op = {"+": lambda a, b: a + b,
    #       "-": lambda a, b: a - b,
    #       "*": lambda a, b: a * b,
    #       "/": lambda a, b: a / b, }
    op = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b, lambda a, b: a / b]
    ops = list(itertools.combinations_with_replacement(op, 3))
    for d in data:
        flag = False
        dd = list(itertools.permutations(d, 4))
        for _d in dd:  # 一种排列
            for o in ops:  # 一种运算顺序
                temp = o[0](_d[0], _d[1])
                temp = o[1](temp, _d[2])
                temp = o[2](temp, _d[3])
                if temp == 24:
                    flag = True
                    break
            if flag:
                break
        if flag:
            print("true")
        else:
            print("false")



_data = [[8.0, 2.0, 4.0, 6.0], [7.0, 7.0, 7.0, 7.0]]

Check24(_data)
