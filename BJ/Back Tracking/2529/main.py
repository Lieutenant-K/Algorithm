import sys
input = sys.stdin.readline

def dfs(idx):
    if idx == k+1:
        global min_str, max_str
        n = "".join(map(str, arr[1:]))
        if int(n) < int(min_str):
            min_str = n
        if int(n) > int(max_str):
            max_str = n
        return

    for i in range(10):
        if i in arr:
            continue

        if (s[idx] == '<' and arr[-1] < i) or (s[idx] == '>' and arr[-1] > i):
            arr.append(i)
            dfs(idx+1)
            arr.pop()

k = int(input())
s = '<' + "".join(input().split())
arr = [-1]
min_str, max_str = "9"*(k+1), "0"
dfs(0)
print(max_str, min_str, sep='\n')