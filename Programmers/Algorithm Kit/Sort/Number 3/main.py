from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    for h in range(max(citations)+1):
        index = bisect_left(citations, h)
        if len(citations[index:]) >= h:
            answer = h
    return answer