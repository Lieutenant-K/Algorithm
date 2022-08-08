def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x: x[1])
    camera = -30001

    for start, end in routes:
        if camera < start:
            answer += 1
            camera = end

    return answer