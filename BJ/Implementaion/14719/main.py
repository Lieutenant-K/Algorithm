import sys
input = sys.stdin.readline

h, w = map(int, input().split())
s = list(map(int, input().split()))
r = 0
for i in range(1, w-1):
    ml, mr = max(s[:i]), max(s[i+1:])
    v = min(ml, mr)
    if s[i] < v:
        r += v-s[i]
print(r)