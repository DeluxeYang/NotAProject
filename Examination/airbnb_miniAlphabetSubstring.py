# 最小子串覆盖
import itertools

def minimumSubstring(s, alphabet):
    alpha_bet = {}
    for x in alphabet:
        alpha_bet[x] = []
    i = 0
    for _s in s:
        if _s in alpha_bet:
            alpha_bet[_s].append(i)
        i += 1
    if len(alphabet) == 1:
        try:
            if s.index(alphabet) != -1:
                return alphabet
        except:
            return ""
    comb = itertools.product(alpha_bet[alphabet[0]], alpha_bet[alphabet[1]])
    for a in alphabet[2:]:
        comb = itertools.product(comb, alpha_bet[a])
        temp = []
        for c in comb:
            temp.append(list(c[0])+[c[1]])
        comb = temp
    _min = 1000000000
    res = 0
    for c in comb:
        _d = max(c) - min(c)
        if _d < _min:
            res = c
            _min = _d
    return s[min(res):max(res)+1]

# minimumSubstring("daadcbddbadac", "abc")
print(minimumSubstring("asdfg", "g"))
