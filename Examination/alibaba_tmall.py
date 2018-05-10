#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
小明是一个爱吃零食的小伙子，平时会在网上购买各种好吃的零食。
一天，小明了解到，在天猫超市上购买不同种类的零食，会有各种各样的优惠活动，
如：满99减50，满188减100，满288减150等等，
每种零食只参与其中一种优惠活动方式，还包邮哦，
但也有条件，就是每种零食只限购一份。小明看了非常心动，
原来天猫超市上购买零食会这么划算，可以节省很多钱，真的太好了。
心动不如行动，小明马上列出了所有参与活动的零食种类和其价格，
以及每种零食种类参与的优惠活动方式，
小明也看了看自己支付宝里面的余额为M（正整数）元，
用于天猫超市上的购物支付。但是小明烦恼也来了，左算右算，
也算不出怎样选择零食的组合才能使自己买到的零食总和价值最大，
聪明的你帮帮小明算算，在最后支付时（优惠后）的总金额不大于M的前提下，
小明最多可以买到零食的价值总和N。
输入数据包括：
（1）优惠活动：满减金额条件和其满减金额（小于或等于5种优惠活动）；
（2）每种零食的价格和其参加的优惠活动（小于30种零食）；
（3）小明支付宝余额M

输出：小明最多可以买到零食的价值总和N
99-50;188-100;288-150
28-1;36-1;46-2;78-1;122-2;59-2;198-3;78-3;27-2;67-1;59-3;211-3
388
"""
from itertools import combinations

coupons_input = "99-50;188-100;288-150".split(";")
coupons = {}
count = 1
for c in coupons_input:
    temp_c = c.split("-")
    temp = {"price": int(temp_c[0]), "off": int(temp_c[1])}
    coupons[count] = temp
    count += 1

items_input = "28-1;36-1;46-2;78-1;122-2;59-2;198-3;78-3;27-2;67-1;59-3;211-3".split(";")
items = []
for i in items_input:
    temp_i = i.split("-")
    temp = {"price": int(temp_i[0]), "coupon": int(temp_i[1])}
    items.append(temp)

M = int(388)

N = []

for i in range(1, len(items)+1):
    # 从1开始的每一种商品数全部组合
    temp_items_combs = combinations(items, i)
    for items_comb in temp_items_combs:
        # 每个组合
        for k in coupons:
            coupons[k]["total"] = 0
        for item in items_comb:
            # 每个商品
            coupons[item["coupon"]]["total"] += item["price"]
        N_temp = 0
        M_temp = 0
        for k in coupons:
            if coupons[k]["total"] >= coupons[k]["price"]:
                M_temp += coupons[k]["total"] - coupons[k]["off"]
            else:
                M_temp += coupons[k]["total"]
            N_temp += coupons[k]["total"]
        if M_temp <= M:
            N.append(N_temp)
print(max(N))
