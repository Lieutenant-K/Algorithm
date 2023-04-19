import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(int(input())):
    a = list(map(int, input().split()))
    n, s = a[0], a[1:]
    r = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] > s[j]:
                r += gcd(s[i], s[j])
            else:
                r += gcd(s[j], s[i])
    print(r)