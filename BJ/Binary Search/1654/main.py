k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

def binary(s, e):

    m = (s + e) // 2
    r = 0

    if s > e:
        return m

    for l in lan:
        r += l // m

    if r >= n:
        return binary(m+1, e)
    else:
        return binary(s, m-1)

print(binary(1, max(lan)))