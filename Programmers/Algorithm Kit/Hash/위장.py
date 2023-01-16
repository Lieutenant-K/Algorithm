from collections import Counter
from functools import reduce
def solution(clothes):
    values = Counter(map(lambda x: x[1], clothes)).values()
    return reduce(lambda x, y: x*(y+1), values, 1)-1
