def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and int(stack[-1]) < int(num):
            stack.pop()
            k -= 1
        stack.append(num)

    return ''.join(stack[:len(stack) - k])