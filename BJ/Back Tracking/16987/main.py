import sys
input = sys.stdin.readline

def function(idx, cnt):
    if idx == n:
        global m
        m = max(m, cnt)
        return

    if s[idx] <= 0 or cnt == n-1:
        function(idx+1, cnt)
        return

    for i in range(n):
        if i != idx and s[i] > 0:
            s[i] -= w[idx]
            s[idx] -= w[i]
            function(idx+1, cnt + int(s[i] <= 0) + int(s[idx] <= 0))
            s[i] += w[idx]
            s[idx] += w[i]

n = int(input())
s, w = [], []
m = 0
for _ in range(n):
    a, b = map(int, input().split())
    s.append(a)
    w.append(b)
function(0, 0)
print(m)