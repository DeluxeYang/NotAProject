"""
给定一个数列，这个数列的特点为第n个数An（n>3）为前三个数之和（An-1 + An-2 + An-3）。
已知这个数列前3个数A1，A2，A3，求第n个数是多少（结果对10000取余）？
"""


def get_n(a1, a2, a3, n):
    l = [a1, a2, a3, 0]
    for i in range(3, n):
        l[3] = l[0] + l[1] + l[2]
        l[0] = l[1]
        l[1] = l[2]
        l[2] = l[3]
    return l[3] % 10000

print(get_n(1234, 5678, 9012, 5))

'''
_a1 = int(raw_input())

_a2 = int(raw_input())

_a3 = int(raw_input())

_n = long(raw_input())

  
res = GetAn(_a1, _a2, _a3, _n)

print str(res) + "\n"
'''
