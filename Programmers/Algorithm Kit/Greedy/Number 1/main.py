def solution(n, lost, reserve):
    uniform = [0] * (n + 2)

    for student in lost:
        uniform[student] -= 1
    for student in reserve:
        uniform[student] += 1

    for student in range(1, n + 1):

        # 여벌의 체육복을 갖고 있는 학생일 때
        if uniform[student] > 0:

            # 앞 학생에게 체육복을 줄 수 있는지 확인
            if uniform[student - 1] < 0:
                uniform[student - 1] += 1
                uniform[student] -= 1
            # 뒤 학생에게 체육복을 줄 수 있는지 확인
            elif uniform[student + 1] < 0:
                uniform[student + 1] += 1
                uniform[student] -= 1

    # 결과적으로 체육복을 갖고 있는 학생들만 모아서 인원을 카운트
    result = [student for student in range(1, n + 1) if uniform[student] >= 0]

    return len(result)