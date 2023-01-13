def solution(brown, yellow):
    widths = [w for w in range(3, 2500) if 2*w**2 - w*(brown+4) + 2*(brown+yellow) == 0]
    return [max(widths), min(widths)]
