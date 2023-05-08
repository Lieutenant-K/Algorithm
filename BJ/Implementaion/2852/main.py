import sys
input = sys.stdin.readline

n = int(input())
score = [0, 0, 0]
winningTime = [0, 0, 0]
last = (0, 0)
for _ in range(n):
    team, time = input().split()
    minute, second = map(int, time.split(':'))
    current = second + minute * 60
    score[int(team)] += 1

    if score[1] == score[2]:
        winningTime[last[0]] += current - last[1]
        last = (0, 0)
    else:
        t = 1 if score[1] > score[2] else 2
        if t != last[0]:
            last = (t, current)

if last[0] > 0:
    winningTime[last[0]] += 48 * 60 - last[1]

for i in range(1, 3):
    m, s = map(str, divmod(winningTime[i], 60))
    print('0'*(2-len(m)) + m + ':' + '0'*(2-len(s)) + s)