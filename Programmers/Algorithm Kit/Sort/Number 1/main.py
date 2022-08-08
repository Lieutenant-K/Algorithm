def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        cut_array = sorted(array[i-1:j])
        answer.append(cut_array[k-1])

    return answer