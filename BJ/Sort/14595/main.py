import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
action = sorted([tuple(map(int, input().split())) for _ in range(M)])
idx = 1
ans = 1
for a, b in action:
    if idx < a:
        ans += a - idx
    idx = max(idx, b)
print(ans + N - idx)

#from collections import deque
# def bfs(idx):
#     visit[idx] = True
#     q = deque([idx])
#     left, right = idx, idx
#     while q:
#         x = q.popleft()
#         if G[x][0] < left:
#             for i in range(G[x][0], left):
#                 if not visit[i]:
#                     visit[i] = True
#                     q.append(i)
#             left = G[x][0]
#         if G[x][1] > right:
#             for i in range(right+1, G[x][1]+1):
#                 if not visit[i]:
#                     visit[i] = True
#                     q.append(i)
#             right = G[x][1]
#     return 1
#
# N = int(input())
# M = int(input())
# G = [[i]*2 for i in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a][1] = max(G[a][1], b)
#     G[b][0] = min(G[b][0], a)
# visit = [False]*(N+1)
# ans = 0
# for i in range(1, N+1):
#     if not visit[i]:
#         ans += bfs(i)
# print(ans)