import sys
input = sys.stdin.readline

n = map(int, input())
A = list(map(int, input().split()))
m = 10**6
p = [True]*(m+1)
for i in range(2, int(m**0.5)+1):
    if not p[i]:
        continue
    j = 2
    while i*j <= m:
        p[i*j] = False
        j += 1

result = 1
for a in set(A):
    if p[a]:
        result *= a

if result == 1:
    print(-1)
else:
    print(result)