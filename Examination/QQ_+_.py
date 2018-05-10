import itertools


def f():
    a = 100
    A = 2000
    op = ["+", "*"]
    i = 0
    ops_list = {}
    while True:
        i += 1
        comb = itertools.combinations_with_replacement(op, i)
        for c in comb:
            permutation = itertools.permutations(c, i)
            for p in permutation:
                temp_a = a
                temp_str = ''
                for _p in p:
                    temp_str += _p
                if temp_str not in ops_list:
                    ops_list[temp_str] = 1
                    for _p in p:
                        if _p == "+":
                            temp_a += 1
                        elif _p == "*":
                            temp_a *= 2
                    if temp_a == A:
                        print("答案：")
                        print(i)
                        print(p)
                        return
f()
