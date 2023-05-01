import sys
input = sys.stdin.readline
from collections import Counter

s = input().rstrip()
dic = Counter(s)
r = ""
for _ in range(len(s)//2):
    for key in sorted(dic.keys()):
        if dic[key] >= 2:
            r += key
            dic[key] -= 2
            break

result = "I'm Sorry Hansoo"
if len(s) % 2 == 0:
    if len([k for k, v in dic.items() if v > 0]) == 0:
        result = r + r[::-1]
else:
    a = [k for k, v in dic.items() if v == 1]
    if len(a) == 1:
        result = r + a[0] + r[::-1]
print(result)