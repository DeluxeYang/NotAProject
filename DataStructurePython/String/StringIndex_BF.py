import SString

def StringIndex_BF(sstring_1, sstring_2, pos=1):
    i, j= pos, 1
    while pos <= sstring_1.string[0] - sstring_2.string[0] + 1 and j <= sstring_2.string[0]:
        if sstring_1.string[i] == sstring_2.string[j]:
            i += 1
            j += 1
        else:
            i = i - j + 2 #回溯, i-j消除了匹配时的滑动，+1是为了算上自己本身，再+1是为了从下一个位置匹配
            j = 1
            pos = i
    if j > sstring_2.string[0]:
        return i - sstring_2.string[0]
    else:
        return False

def StringIndex_KMP(sstring_1, sstring_2, pos=1):
    i, j= pos, 1
    KMP_next = get_KMP_next(sstring_2)
    while pos <= sstring_1.string[0] - sstring_2.string[0] + 1 and j <= sstring_2.string[0]:
        if j ==0 or sstring_1.string[i] == sstring_2.string[j]:
            i += 1
            j += 1
        else:
            j = KMP_next[j]
            pos = i
    if j > sstring_2.string[0]:
        return i - sstring_2.string[0]
    else:
        return 0

def get_KMP_next(sstring):
    KMP_next = [0] * (sstring.string[0] + 1)
    j, k = 1, 0
    while j < sstring.string[0]:
        if k == 0 or sstring.string[j] == sstring.string[k]:
            j += 1
            k += 1
            KMP_next[j] = k
        else:
            k = KMP_next[k]
    return KMP_next


if __name__ == '__main__':
    S_TEST = SString.SString(100)
    S_TEST.assign("abcdabd")
    S_TEST1 = S_TEST.sub_string(2,5)

    S_TEST1.traverse()
    print(get_KMP_next(S_TEST))

    print(StringIndex_KMP(S_TEST,S_TEST1))