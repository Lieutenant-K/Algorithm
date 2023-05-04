import sys
input = sys.stdin.readline

def dfs(sub, target):
    if sub == target:
        return 1

    if d.get(sub) is not None:
        return d[sub]

    start, end = 0, len(target)
    subset = set()
    while(1):
        idx = target.find(sub, start, end)
        length = len(sub) if len(sub) > 0 else 1

        if idx == -1:
            break

        if idx - 1 >= 0:
            subset.add(target[idx-1] + sub)
        if idx + length < len(target):
            subset.add(sub + target[idx+length])

        start = idx + 1

    r = 0
    for s in subset:
        r += dfs(s, target)
    d[sub] = r

    return r


n = input().rstrip()
d = dict()
print(dfs("", n))