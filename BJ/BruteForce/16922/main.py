import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n = int(input())
comb = list(combinations_with_replacement("IVXL", n))
dic = {"I": 1, "V": 5, "X": 10, "L": 50}
print(len(set([sum(map(lambda x:dic[x], c)) for c in comb])))

