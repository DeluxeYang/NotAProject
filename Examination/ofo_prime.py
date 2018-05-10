"""

分解质因数是我们常用的数学方法，它是把一个合数分解成若干个质因数的乘积的形式。
求一个数分解质因数，要从最小的质数除起，一直除到结果为质数为止。借助计算机程序，我们可以快速的完成质因数分解。
为了简单起见，给定一个正整数n，求这个正整数n分解质因数后最大的那个质因数是多少（若n为质数，则输出n本身）？
"""

import math

temp_list = []


def MaxFactor(n):
    is_prime = True
    i = 2
    square = int(math.sqrt(n)) + 1
    while i <= square:
        if n % i == 0:
            temp_list.append(i)
            is_prime = False
            MaxFactor(n / i)
            i += 1
            break
        i += 1
    if is_prime:
        temp_list.append(n)



MaxFactor(123456)

print(int(max(temp_list)))
