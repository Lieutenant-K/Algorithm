def solution(sizes):
    return max([min(w, h) for w, h in sizes])*max(max(w, h) for w, h in sizes)
