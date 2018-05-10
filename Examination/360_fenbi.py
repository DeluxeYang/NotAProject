#!/bin/python
"""
小明一共有n根彩色粉笔，m根白色粉笔，
现在可以用a根彩色粉笔和b根白色粉笔组成一盒卖x元，
或者c根白色粉笔组成一盒卖y元，或者d根彩色粉笔组成一盒卖z元，
小明最多可以用这些粉笔卖多少元？
不一定要把所有粉笔卖完，小明只希望利益最大化。

第一行2个整数n，m，1≤n,m≤2000；
第二行4个整数a，b，c，d，1≤a,b,c,d≤1000；
第三行3个整数x，y，z，1≤x,y,z≤1000。

5 5
1 2 3 3
2 1 3
"""
import itertools
n = 5  # 彩
m = 5  # 白
a = 1
b = 2
c = 3
d = 3
x = 2
y = 1
z = 3

A = {"white": b, "color": a, "price": x}
B = {"white": c, "color": 0, "price": y}
C = {"white": 0, "color": d, "price": z}
_sales = [A, B, C]


def f(_color, _white, sales):
    rl = []
    for _sales in itertools.permutations(sales, 3):  # 列举所有
        S = 0
        color = _color
        white = _white
        for s in _sales:
            temp_white = white // s["white"] if s["white"] != 0 else 0
            temp_color = color // s["color"] if s["color"] != 0 else 0
            if temp_color == temp_white:
                white -= temp_white*s["white"]
                color -= temp_color * s["color"]
                S += temp_white * s["price"]
            elif temp_color > temp_white:
                if temp_white == 0:
                    color -= temp_color * s["color"]
                    S += temp_color * s["price"]
                white -= temp_white * s["white"]
                color -= temp_white * s["color"]
                S += temp_white * s["price"]
            else:
                if temp_color == 0:
                    white -= temp_white * s["white"]
                    S += temp_white * s["price"]
                white -= temp_color * s["white"]
                color -= temp_color * s["color"]
                S += temp_color * s["price"]
        rl.append(S)
    return max(rl)

print(f(n, m, _sales))

