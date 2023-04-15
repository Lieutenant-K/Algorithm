import sys
input = sys.stdin.readline

for _ in range(int(input())):
    crying = input().rstrip().split()
    cries = set()
    while 1:
        s = input().rstrip()

        if s == "what does the fox say?":
            break

        cry = (s.split())[2]
        cries.add(cry)

    print(*[c for c in crying if c not in cries])