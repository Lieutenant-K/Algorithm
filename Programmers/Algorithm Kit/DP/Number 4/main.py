def solution(money):
    answer = 0
    n = len(money)
    d1 = [money[0], max(money[0], money[1])] + [0]*(n-2)
    d2 = [0, money[1]] + [0]*(n-2)
    for i in range(2, n):
        if i < n-1:
            d1[i] = max(d1[i-2] + money[i], d1[i-1])
        d2[i] = max(d2[i-2] + money[i], d2[i-1])
    return max(max(d1), max(d2))