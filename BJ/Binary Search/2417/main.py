n = int(input())
s, e, p = 0, n, 0
while s <= e:
    p = (s+e)//2
    if p*p > n:
        e = p-1
    elif p*p == n:
        break
    else:
        s = p+1
if p*p < n:
    p += 1
print(p)