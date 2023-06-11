import sys
input = sys.stdin.readline

def next_permutations(arr):
    s, e = 0, 0
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            s = i
            break

    for i in range(len(arr)-1, -1, -1):
        if arr[s] < arr[i]:
            e = i
            break

    arr[s], arr[e] = arr[e], arr[s]

    if s == e:
        return arr
    else:
        return arr[:s+1] + arr[:s:-1]


for _ in range(int(input())):
    word = list(input().rstrip())
    print("".join(next_permutations(word)))