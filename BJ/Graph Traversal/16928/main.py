import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
board = [0]*101
for _ in range(n+m):
    s, e = map(int, input().split())
    dic[s] = e
queue = deque([1])
while queue:
    x = queue.popleft()
    # 주사위를 굴려서 갈 수 있는 칸들
    for i in range(1, 7):
        # 검사하는 칸이 보드판 범위 안에 있고 아직 방문하지 않았으면
        if x+i <= 100:
            if x+i in dic.keys() and board[dic[x+i]] == 0:
                board[dic[x+i]] = board[x]+1
                queue.append(dic[x+i])
            elif x+i not in dic.keys() and board[x+i] == 0:
                board[x + i] = board[x] + 1
                queue.append(x+i)
print(board[100])
