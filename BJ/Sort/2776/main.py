import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, an = int(input()), set(map(int, input().split()))
    m, am = int(input()), list(map(int, input().split()))
    for e in am:
        print(1 if e in an else 0)