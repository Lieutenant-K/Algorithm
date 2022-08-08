import heapq
from collections import deque
def solution(jobs):
    h = []
    n = len(jobs)
    tasks = deque(sorted(jobs))
    end, answer = tasks.popleft()
    end += answer

    while len(tasks) > 0:
        start, time = tasks[0]
        if start <= end:
            heapq.heappush(h, (time, start))
            tasks.popleft()
        else:
            if len(h) > 0:
                t, s = heapq.heappop(h)
                answer += (end - s) + t
                end += t
            else:
                answer += time
                end = start + time
                tasks.popleft()
    while len(h) > 0:
        t, s = heapq.heappop(h)
        answer += (end - s) + t
        end += t
    return answer//n