import sys
input = sys.stdin.readline

def solution(name):
    up_down = [min(ord(char)-65, 91-ord(char)) for char in name]
    n = len(name)
    count = n-1
    for i in range(n):
        index = i+1
        while index < n and name[index] == 'A':
            index += 1
        count = min(count, i+(i+n-index), 2*(n-index)+i)

    answer = sum(up_down) + count
    print(answer)

for _ in range(int(input())):
    solution(input().rstrip())