def solution(sizes):
    for size in sizes:
        size.sort()
    resize = list(zip(*sizes))
    return max(resize[0])*max(resize[1])