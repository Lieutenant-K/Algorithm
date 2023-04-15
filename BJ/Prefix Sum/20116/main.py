import sys
input = sys.stdin.readline

N, L = map(int, input().split())
x = list(map(int, input().split()))
total = 0
for i in range(N-1, 0, -1):
    total += x[i]
    if x[i-1] - L < total / (N-i) < x[i-1] + L:
        continue
    else:
        print("unstable")
        exit()
print("stable")