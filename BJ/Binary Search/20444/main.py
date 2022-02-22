import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s, e = 0, n//2

while s <= e:
    m = (s+e)//2
    v = (m+1)*(n-m+1)

    if v > k:
        e = m-1
    elif v == k:
        print("YES")
        exit()
    else:
        s = m+1
print("NO")