import heapq
def solution(operations):
    h = []
    for oper in operations:
        alpha, number = str(oper).split(' ')
        if alpha == 'I':
            heapq.heappush(h, int(number))
        elif alpha == 'D' and h:
            if int(number) > 0:
                h.remove(max(h))
                heapq.heapify(h)
            else:
                heapq.heappop(h)
    if h:
        return [max(h), h[0]]
    else:
        return [0, 0]