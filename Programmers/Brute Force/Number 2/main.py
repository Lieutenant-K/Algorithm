from itertools import permutations

m = 10 ** 7
p = [True for i in range(m)]
p[0] = p[1] = False
for i in range(2, int(m ** 0.5) + 1):
    if p[i]:
        j = 2
        while i * j < m:
            p[i * j] = False
            j += 1


def solution(numbers):
    answer = 0
    primary = set([])

    length = len(numbers)
    for cnt in range(1, length + 1):
        permutation = set(permutations(numbers, cnt))
        for number in permutation:
            num = int(''.join(number))
            if p[num]:
                primary.add(num)

    answer = len(primary)
    return answer