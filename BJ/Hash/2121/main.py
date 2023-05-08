import sys
input = sys.stdin.readline

n = int(input())
A, B = map(int, input().split())
p = set([tuple(map(int, input().split())) for _ in range(n)])
r = 0
for x, y in p:
    if (x+A, y) in p and (x, y+B) in p and (x+A, y+B) in p:
        r += 1
print(r)