def solution(brown, yellow):
    for n in range(1, int(yellow**0.5)+1):
        if yellow % n == 0:
            w, h = yellow//n, n
            if (w+2)*2 + h*2 == brown:
                return [w+2, h+2]