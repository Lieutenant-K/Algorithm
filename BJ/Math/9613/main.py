import sys
input = sys.stdin.readline

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

for _ in range(int(input())):
    arr = list(map(int, input().split()))
    n, numbers = arr[0], arr[1:]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += gcd(numbers[i], numbers[j])
    print(ans)