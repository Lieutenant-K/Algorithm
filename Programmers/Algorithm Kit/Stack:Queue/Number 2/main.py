from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(list(enumerate(priorities)))
    while len(queue) > 0:
        index, prior = queue[0]
        if prior >= (max(queue, key=lambda x: x[1]))[1]:
            answer += 1
            queue.popleft()
            if index == location:
                return answer
        else:
            queue.rotate(-1)