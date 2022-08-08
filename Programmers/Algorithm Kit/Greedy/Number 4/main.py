def solution(people, limit):
    answer = 0

    people = sorted(people)
    left, right = 0, len(people) - 1
    while left < right:
        sum = people[left] + people[right]
        if sum <= limit:
            left += 1
        right -= 1
        answer += 1
    if left == right:
        answer += 1

    return answer