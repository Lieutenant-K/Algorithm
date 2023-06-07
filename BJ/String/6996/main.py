import sys
from collections import Counter
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = input().split()
    if set(Counter(A).items()) == set(Counter(B).items()):
        print(A + " & " + B + " are anagrams.")
    else:
        print(A + " & " + B + " are NOT anagrams.")