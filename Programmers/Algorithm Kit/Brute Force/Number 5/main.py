from itertools import product

def solution(word):
    return sorted(["".join(p) for i in range(5) for p in product("AEIOU", repeat=i+1)]).index(word)+1