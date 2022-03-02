import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    k = int(input())
    d = [[] for _ in range(26)]

    for i in range(len(s)):
        d[ord(s[i]) - 97].append(i)

    mi, mx = 10001, -1
    for c in d:
        if len(c) >= k:
            i = 0
            while i+k <= len(c):
                v = c[i+k-1]-c[i]+1
                mi = min(mi, v)
                mx = max(mx, v)
                i += 1

    if mi*mx < 0:
        print(-1)
    else:
        print(mi, mx)