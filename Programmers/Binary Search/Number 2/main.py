def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    s, e = 1, distance
    while s <= e :
        m = (s+e) // 2
        cnt, d = 0, 0
        for rock in rocks:
            if rock-d < m:
                cnt += 1
            else:
                d = rock
        if cnt > n :
            e = m-1
        else:
            answer = m
            s = m+1
    return answer