import math
def solution(progresses, speeds):
    answer = []
    stack = []
    n = len(speeds)
    for day in [math.ceil((100 - progresses[i])/speeds[i]) for i in range(n)]:
        if len(stack) == 0 or stack[-1] < day:
            answer.append(1)
            stack.append(day)
        else:
            answer[-1] += 1
    return answer
