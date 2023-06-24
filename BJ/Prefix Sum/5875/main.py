import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
s = " " + s + " "
o, c = [0]*(n+2), [0]*(n+2)
dic = {'(': 1, ')': -1}
for i in range(1, n+1):
    k = o[i-1] + dic[s[i]]
    p = c[i-1] + (-1)*dic[s[n+1-i]]
    if k >= 0:
        o[i] = k
    if p >= 0:
        c[i] = p
c = c[:1] + list(reversed(c[1:n+1])) + c[n+1:]

r = 0
for i in range(1, n+1):
    if s[i] == '(':
        if o[i-1] > 0 and o[i-1]-1 == c[i+1]:
            r += 1
    else:
        if c[i+1] > 0 and c[i+1]-1 == o[i-1]:
            r += 1
print(r)