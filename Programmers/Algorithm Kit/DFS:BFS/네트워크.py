from collections import deque
def solution(n, computers):
    answer = 0
    check = [True]*n
    for i in range(n):
        if check[i]:
            check[i] = False
            answer += 1
            queue = deque([i])
            while queue:
                c = queue.popleft()
                for j in range(n):
                    if check[j] and computers[c][j]:
                        check[j] = False
                        queue.append(j)
    return answer
