import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))
robot = [False]*2*n
t = 1
cnt = 0
while(1):
    A = A[-1:] + A[:-1]
    robot = robot[-1:] + robot[:-1]
    robot[n-1] = False

    for i in range(n-1, -1, -1):
        if robot[i] and not robot[i+1] and A[i+1] > 0:
            A[i+1] -= 1
            if A[i+1] == 0:
                cnt += 1
            robot[i] = False
            robot[i+1] = True
    robot[n-1] = False

    if A[0] > 0:
        robot[0] = True
        A[0] -= 1
        if A[0] == 0:
            cnt += 1

    if cnt >= k:
        print(t)
        break

    t += 1