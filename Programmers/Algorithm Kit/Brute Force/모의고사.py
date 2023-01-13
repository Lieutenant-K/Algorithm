def solution(answers):
    supo = [0, 0, 0]
    for index, answer in enumerate(answers):
        check = [(index % 5) + 1, 2 if index % 2 == 0 else [1, 3, 4, 5][(index//2) % 4], [3, 1, 2, 4, 5][(index//2) % 5]]
        for i in range(3):
            supo[i] += bool(answer == check[i])
    return [i+1 for i, m in enumerate(supo) if m == max(supo)]
