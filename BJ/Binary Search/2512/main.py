n = int(input())
fund = list(map(int, input().split()))
c = int(input())
def binary(s, e):
    m = (s + e) // 2
    r = 0

    if s > e:
        return m

    for f in fund:
        if f >= m:
            r += m
        else:
            r += f

    if r <= c:
        return binary(m+1, e)
    else:
        return binary(s, m-1)

print(binary(1, max(fund)))