import sys
input = sys.stdin.readline

n = int(input())
v = list(map(int, input().split()))
s, e = 1, (10**9)*(3*10**5)
r = 0
while s <= e:
    m = (s + e) // 2
    k, flag = m, True

    for i in range(n):
        if k < v[i]:
            flag = False
            break
        k = v[i] * (k // v[i])

    if flag:
        e = m-1
        r = m
    else:
        s = m+1
print(r)