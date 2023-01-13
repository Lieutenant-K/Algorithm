from itertools import product
from functools import reduce
def solution(word):
    return sorted(reduce(lambda x, y: x+y, [list(map("".join, product("AEIOU", repeat=i))) for i in range(1, 6)], [])).index(word)+1
