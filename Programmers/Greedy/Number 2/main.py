def find_closest_alphabet(index, alphabets):
    alphabets[index] = False
    changes = alphabets[index:] + alphabets[:index]
    n = len(alphabets)
    count = n
    for i in range(1, n//2+1):
        left, right = n-i, i

        if changes[right]:
            count = min(count, i + find_closest_alphabet(right, changes[:]))
        if changes[left]:
            count = min(count, i + find_closest_alphabet(left, changes[:]))

        # return count
    if count == n:
        return 0

    return count


def solution(name):
    up_down = [min(ord(char)-65, 91-ord(char)) for char in name]
    left_right = [bool(ord(char)-65) for char in name]
    answer = sum(up_down) + find_closest_alphabet(0, left_right)

    return answer


s = "BBBBAAAABA"
print(solution(s))