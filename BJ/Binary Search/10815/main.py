n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

for f in find:
    s, e = 0, n-1
    while s <= e:
        mid = (s+e)//2
        if card[mid] > f:
            e = mid-1
        elif card[mid] == f:
            print(1,end=' ')
            break
        else:
            s = mid+1
    if s > e:
        print(0,end=' ')