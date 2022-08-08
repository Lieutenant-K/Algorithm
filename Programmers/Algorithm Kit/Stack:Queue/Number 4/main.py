def solution(prices):
    n = len(prices)
    answer, stack = [0]*n, []
    for i in range(n):
        while len(stack) > 0 and (prices[stack[-1]] > prices[i] or i == n-1):
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)
    return answer