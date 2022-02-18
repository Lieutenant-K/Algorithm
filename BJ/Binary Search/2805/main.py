n, m = map(int, input().split())
tree = list(map(int, input().split()))

def binary(s, e):

    mid = (s + e) // 2
    r = 0

    if s > e:
        return mid

    for t in tree:
        if t > mid:
            r += t - mid

    if r >= m:
        return binary(mid+1, e)
    else:
        return binary(s, mid-1)

print(binary(0, int(1e9)))