import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(participant, completion):
    dict = defaultdict(int)
    for person in participant:
        dict[person] += 1
    for person in completion:
        dict[person] -= 1
    for key, value in dict.items():
        if value > 0:
            return key