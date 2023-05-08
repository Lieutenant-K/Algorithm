import sys
input = sys.stdin.readline

while(True):
    s = input().rstrip()
    if s == '*':
        break
    n = len(s)
    d = [set() for _ in range(n-1)]
    flag = True
    for i in range(n-1):
        for j in range(i+1, n):
            if (s[i], s[j]) in d[j-i-1]:
                flag = False
            else:
                d[j-i-1].add((s[i], s[j]))
 
    if flag:
        print(s + " is surprising.")
    else:
        print(s + " is NOT surprising.")