import sys
from itertools import combinations
input = sys.stdin.readline

def sol(x):

    m = len(x)
    cnt = len([i for i in x if int(i) % 2 != 0])
    rl, rg = m, 0

    if m == 1:
        return cnt, cnt
    elif m == 2:
        rl, rg = sol(str(int(x[0]) + int(x[1])))
    else:
        for a, b in list(combinations(range(1, m), 2)):
            s = int(x[:a]) + int(x[a:b]) + int(x[b:])
            l, g = sol(str(s))
            rl, rg = min(rl, l), max(rg, g)

    return cnt+rl, cnt+rg


n = input().rstrip()
print(*sol(n), sep=' ')