from itertools import permutations
def solution(k, dungeons):
    n = len(dungeons)
    answer = -1
    for case in list(permutations(list(range(n)))):
        number, cnt = k, 0
        for index in case:
            if number < dungeons[index][0]:
                break
            number -= dungeons[index][1]
            cnt += 1
        answer = max(cnt, answer)

    return answer