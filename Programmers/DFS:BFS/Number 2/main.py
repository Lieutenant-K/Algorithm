from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False]*n
    connect = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j]:
                connect[i].append(j)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            queue = deque([i])
            while queue:
                com = queue.popleft()
                for j in connect[com]:
                    if not visited[j]:
                        visited[j] = True
                        queue.append(j)
            answer += 1
    return answer
