import sys
input = sys.stdin.readline
from collections import deque

def index(i):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    corner = set([(i, i), (i, M-i-1), (N-i-1, M-i-1), (N-i-1, i)])
    
    x, y = i, i
    d = -1
    result = []
    while i <= x < N-i and i <= y < M-i:
        if (x, y) in corner:
            d += 1
        
        if d == 4:
            break
            
        result.append((x, y))
        x = x + dx[d]
        y = y + dy[d]

    return result

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [[0]*M for _ in range(N)]
for i in range(min(N, M) // 2):
    idx = index(i)
    arr = deque([A[a][b] for a, b in idx])
    arr.rotate(-R)
    for j in range(len(idx)):
        x, y = idx[j]
        B[x][y] = arr[j]

for row in B:
    print(" ".join(map(str, row)))