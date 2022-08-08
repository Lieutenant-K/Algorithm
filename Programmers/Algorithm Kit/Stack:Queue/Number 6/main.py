def solution(s):
    cnt = 0
    for g in s:
        if cnt < 0:
            break
        cnt = cnt+1 if g == '(' else cnt-1
    return cnt == 0