def solution(k, dungeons):
    m = 0
    for require, use in dungeons:
        if k >= require:
            new = dungeons[:]
            new.remove([require, use])
            m = max(m, 1+solution(k-use, new))
    return m
