import sys
input = sys.stdin.readline


def dfs(length, cnt, result):
    if cnt == 2:
        global answer
        answer = max(result, answer)
        return

    # k = min(h, w) if min(h, w) != 0 else 1
    # a = k if k % 2 != 0 else k - 1

    for l in range(length, 0, -2):

        # if l > pre:
        #     continue

        for x in range(n):

            if x + l - 1 >= n:
                break

            for y in range(m):

                if y + l - 1 >= m:
                    break

                ho = g[x + l // 2][y:y + l]
                ve = list(zip(*g))[y + l // 2][x:x + l]

                if '.' not in set(ho) and '.' not in set(ve):
                    for r in range(l):
                        g[x + r][y + l // 2] = '.'
                    for c in range(l):
                        g[x + l // 2][y + c] = '.'

                    dfs(length, cnt + 1, result * (2 * l - 1))

                    for r in range(l):
                        g[x + r][y + l // 2] = ve[r]
                    for c in range(l):
                        g[x + l // 2][y + c] = ho[c]


n, m = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
answer = 0
k = min(n, m) if min(n, m) % 2 != 0 else min(n, m)-1
dfs(k, 0, 1)
print(answer)