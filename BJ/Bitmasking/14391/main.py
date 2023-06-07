import sys
input = sys.stdin.readline

def bitmask():
    answer = 0
    for i in range(1 << N*M):
        result = 0
        for row in range(N):
            horizon_sum = 0
            for column in range(M):
                idx = row * M + column
                if i & (1 << idx) != 0:
                    horizon_sum = horizon_sum * 10 + G[row][column]
                else:
                    result += horizon_sum
                    horizon_sum = 0
            result += horizon_sum

        for column in range(M):
            vertical_sum = 0
            for row in range(N):
                idx = row * M + column
                if i & (1 << idx) == 0:
                    vertical_sum = vertical_sum * 10 + G[row][column]
                else:
                    result += vertical_sum
                    vertical_sum = 0
            result += vertical_sum
        answer = max(answer, result)
    return answer


print(2**16 * 16)
N, M = map(int, input().split())
G = [list(map(int, list(input().rstrip()))) for _ in range(N)]
print(bitmask())