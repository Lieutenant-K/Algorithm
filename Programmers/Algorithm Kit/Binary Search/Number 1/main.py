def solution(n, times):
    answer = 0
    s, e = 1, max(times)*n
    while s <= e:
        m = (s+e)//2
        r = sum([m//t for t in times])
        if r >= n:
            answer = m
            e = m-1
        else:
            s = m+1
    return answer