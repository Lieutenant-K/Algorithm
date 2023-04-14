import sys
input = sys.stdin.readline

g = [list(map(int, input().split())) for _ in range(9)]
row = []
column = []
grid = []
blank = []
for i in range(9):
    row.append(set([e for e in g[i] if e != 0]))
    column.append(set([e for e in list(zip(*g))[i] if e != 0]))
    cell = []
    for j in range(3*(i//3), 3*(i//3)+3):
        for k in range(3*(i % 3), 3*(i % 3)+3):
            if g[j][k] != 0:
                cell.append(g[j][k])
            else:
                blank.append((j, k))
    grid.append(set(cell))

def dfs(idx):
    if idx == len(blank):
        for r in g:
            print(*r, sep=" ", end="\n")
        exit()

    x, y = blank[idx]
    i = 3 * (x // 3) + (y // 3)
    for n in range(1, 10):
        if n in row[x] or n in column[y]:
            continue
        if n in grid[i]:
            continue

        row[x].add(n)
        column[y].add(n)
        grid[i].add(n)
        g[x][y] = n

        dfs(idx+1)

        row[x].remove(n)
        column[y].remove(n)
        grid[i].remove(n)
        g[x][y] = 0

dfs(0)

