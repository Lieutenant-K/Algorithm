import sys
input = sys.stdin.readline

while(1):
    s = input().rstrip()

    if s == ".":
        break

    stack = []
    dic = {')': '(', ']':'['}
    result = True
    for c in s:
        if c in dic.values():
            stack.append(c)
        elif c in dic.keys():
            if stack and stack[-1] == dic[c]:
                stack.pop()
            else:
                result = False
                break
    print("yes" if result and not stack else "no")