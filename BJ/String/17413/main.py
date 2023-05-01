import sys
input = sys.stdin.readline

s = input().rstrip()
r = ""

for s in s.split('<'):
    sub = s.split('>')
    if len(sub) == 2:
        tag = '<' + sub[0] + '>'
        words = " ".join([e[::-1] for e in sub[1].split()])
        r += tag + words
    else:
        words = " ".join([e[::-1] for e in sub[0].split()])
        r += words
print(r)