import sys
input = sys.stdin.readline

def find_element(r, c):
    global cnt
    
    result = 0
    if abs(r) >= abs(c):
        if r < 0:
            v = 1 + sum([8*i - 5 for i in range(1, abs(r)+1)])
            result = v - c
        else:
            v = 1 + sum([8*i - 1 for i in range(1, abs(r)+1)])
            result = v + c
    else:
        if c < 0:
            v = 1 + sum([8*i - 3 for i in range(1, abs(c)+1)])
            result = v + r
        else:
            v = 1 + sum([8*i - 7 for i in range(1, abs(c)+1)])
            result = v - r

    cnt = max(cnt, len(str(result)))
    return result

r1, c1, r2, c2 = map(int, input().split())
cnt = 0
s = [[find_element(r, c) for c in range(c1, c2+1)] for r in range(r1, r2+1)]
for r in s:
    print(*map(lambda x: " " * (cnt - len(x)) + x, map(str, r)), sep=" ")