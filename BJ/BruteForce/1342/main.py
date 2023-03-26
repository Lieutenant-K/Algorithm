import sys
from collections import Counter
input = sys.stdin.readline

def dfs(pre, info):
    keys = set(info.keys())

    if len(keys) == 0:
        return 1

    r = 0
    keys -= {pre}
    for key in keys:
        update = info.copy()
        update[key] -= 1
        if update[key] == 0:
            update.pop(key)
        r += dfs(key, update)
    return r

s = input().rstrip()
dic = dict(Counter(s))
print(dfs("A", dic))
