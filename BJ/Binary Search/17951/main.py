import sys
input = sys.stdin.readline

n, k = map(int, input().split())
test = list(map(int, input().split()))
s, e = 0, sum(test)
answer = 0
while s <= e:
    m = (s + e) // 2
    r, cnt = 0, 0
    for i in test:
        r += i
        if r >= m:
            cnt += 1
            r = 0

    if cnt >= k:
        s = m+1
        answer = m
    else:
        e = m-1
print(answer)