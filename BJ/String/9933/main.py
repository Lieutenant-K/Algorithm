import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
for w in words:
    if w[::-1] in words:
        print(len(w), w[len(w)//2])
        exit()