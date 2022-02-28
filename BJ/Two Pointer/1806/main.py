n, S = map(int, input().split())
s = list(map(int, input().split()))

a, b, r = 0, 0, 10**5
v = 0
while a <= b:
    if v >= S:
        r = min(r, b-a)
        v -= s[a]
        a += 1
    elif b == n:
        break
    else:
        v += s[b]
        b += 1
print(r % 10**5)