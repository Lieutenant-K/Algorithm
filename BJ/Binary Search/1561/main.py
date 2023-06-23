import sys
input = sys.stdin.readline

N, M = map(int, input().split())
time = list(map(int, input().split()))
s, e = 0, 30*N
t = 0
# N번째 인원이 놀이기구를 탄 인원에 포함되는 최소 시간 찾기
while s <= e:
    # m분 일 때 현재까지 놀이기구를 탄 인원 수
    m = (s + e) // 2
    cnt = sum([m // time[i] + 1 for i in range(M)])

    # N번째 인원이 놀이기구를 탔다면
    if cnt >= N:
        e = m-1
        t = m
    else:
        s = m+1

if t > 0:
    # t-1분까지 놀이기구에 탄 인원 수 계산
    cnt = sum([(t-1) // time[i] + 1 for i in range(M)])

    # 번호가 작은 놀이기구부터 탑승
    for i in range(M):
        cnt += int(t % time[i] == 0)
        if cnt == N:
            print(i+1)
            break
else:
    print(N)