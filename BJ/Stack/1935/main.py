import sys
input = sys.stdin.readline

n = int(input())
op = input().rstrip()
m = [int(input()) for _ in range(n)]
s = []
for o in op:
    if 'A' <= o <= 'Z':
        s.append(m[ord(o) - ord('A')])
        continue

    a, b = s.pop(), s.pop()
    if o == '+':
        v = b + a
    elif o == '-':
        v = b - a
    elif o == '*':
        v = b * a
    else:
        v = b / a
    s.append(v)
print("%.2f" % s[-1])