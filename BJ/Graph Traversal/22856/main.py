import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def search(x):
    left, right = tree[x]
    if left > 0:
        search(left)
    check.append(x)
    if right > 0:
        search(right)

def similar(x):
    left, right = tree[x]
    global cnt
    if left > 0:
        cnt += 1
        similar(left)
    if right > 0:
        cnt += 1
        similar(right)
    if x == check[-1]:
        print(cnt)
        exit()
    cnt += 1


n = int(input())
tree = [[-1, -1] for _ in range(n+1)]
check = []
cnt = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a][0] = b
    tree[a][1] = c

search(1)
similar(1)