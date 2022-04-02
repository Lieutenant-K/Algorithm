def solution(answers):
    length = len(answers)
    p1, p2, p3 = 0, 0, 0

    r2 = [1, 3, 4, 5]
    r3 = [3, 1, 2, 4, 5]

    for i in range(length):
        if answers[i] == (i % 5) + 1:
            p1 += 1

        if i % 2 == 0 and answers[i] == 2:
            p2 += 1
        elif i % 2 != 0 and answers[i] == r2[(i % 8) // 2]:
            p2 += 1

        if answers[i] == r3[(i % 10) // 2]:
            p3 += 1

    r = [p1, p2, p3]
    answer = [i + 1 for i in range(3) if r[i] == max(r)]

    return answer