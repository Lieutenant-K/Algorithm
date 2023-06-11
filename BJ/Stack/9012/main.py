import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    arr = []
    cnt = 0
    for char in s:
        if char == '(':
            arr.append(char)
            cnt += 1
        else:
            cnt -= 1
            if arr:
                arr.pop()

    if not arr and cnt == 0:
        print("YES")
    else:
        print("NO")