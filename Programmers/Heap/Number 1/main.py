import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        not_spicy = heapq.heappop(scoville)
        if not_spicy >= K:
            break
        if len(scoville) == 0:
            return -1
        second_not_spicy = heapq.heappop(scoville)
        heapq.heappush(scoville, not_spicy + second_not_spicy*2)
        answer += 1

    return answer