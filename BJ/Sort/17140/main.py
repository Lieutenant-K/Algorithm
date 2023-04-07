import sys
input = sys.stdin.readline
from collections import Counter

def operate(o):
    result = []
    len_max = 0
    a = A if o == 1 else list(zip(*A))

    for row in a:
        array = sorted([[key, value] for key, value in Counter(row).items() if key != 0])
        temp = []
        for key, value in sorted(array, key=lambda x: x[1]):
            temp += [key, value]

        if len(temp) > len_max:
            len_max = len(temp)

        result.append(temp)

    for row in result:
        row += (len_max - len(row)) * [0]
        if len(row) > 100:
            row = row[:100]

    return result if o == 1 else [list(i) for i in zip(*result)]

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
for t in range(101):
    n, m = len(A), len(A[0])

    if 0 <= r-1 < n and 0 <= c-1 < m and A[r-1][c-1] == k:
        print(t)
        exit()

    op = 1 if n >= m else -1
    A = operate(op)
print(-1)