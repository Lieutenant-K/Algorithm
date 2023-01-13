import itertools
def solution(numbers):
    n = len(numbers)
    elements = set()
    for i in range(1, n+1):
        elements |= set(map(int, map("".join, itertools.permutations(numbers, i))))
    for i in range(2, int(max(elements)**0.5)+1):
        elements -= set(range(i*2, max(elements)+1, i))
    elements -= {0, 1}
    return len(elements)
