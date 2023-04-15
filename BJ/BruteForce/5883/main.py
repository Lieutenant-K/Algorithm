import sys
input = sys.stdin.readline

n = int(input())
line = [int(input()) for _ in range(n)]
result = 0
for storage in set(line):
    removed_line = [s for s in line if s != storage]
    cnt = 0
    pre = removed_line[0]
    for s in removed_line:
        if pre == s:
            cnt += 1
        else:
            pre = s
            result = max(result, cnt)
            cnt = 1
    result = max(result, cnt)
print(result)