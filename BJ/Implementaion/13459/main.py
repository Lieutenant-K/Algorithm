import sys
input = sys.stdin.readline

# 하, 상, 우, 좌
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def straight(x, y, d):
    nx, ny = x, y
    while g[nx + dx[d]][ny + dy[d]] in ['.', 'O']:
        nx += dx[d]
        ny += dy[d]
        # 구멍에 빠졌다면, 구멍의 좌표를 반환
        if g[nx][ny] == 'O':
            return nx, ny
    return nx, ny

def collapse(first, second, d):
    fx, fy = first
    sx, sy = second
    move_fx, move_fy = straight(fx, fy, d)
    if (move_fx, move_fy) != hole:
        g[move_fx][move_fy] = '#'
        move_sx, move_sy = straight(sx, sy, d)
        g[move_fx][move_fy] = '.'
    else:
        move_sx, move_sy = straight(sx, sy, d)
    return (move_fx, move_fy), (move_sx, move_sy)

def move(r, b, d):
    rx, ry = r
    bx, by = b
    # 두 구슬이 같은 행에 있고, 좌우로 기울일 경우
    if rx == bx and d >= 2:
        # 우로 기울일 경우
        if d == 2:
            if ry < by:
                nb, nr = collapse(b, r, d)
            else:
                nr, nb = collapse(r, b, d)
            return nr, nb
        # 좌로 기울일 경우
        else:
            if ry < by:
                nr, nb = collapse(r, b, d)
            else:
                nb, nr = collapse(b, r, d)
            return nr, nb
    # 두 구슬이 같은 열에 있고, 상하로 기울일 경우
    elif ry == by and d < 2:
        # 하로 기울길 경우
        if d == 0:
            if rx < bx:
                nb, nr = collapse(b, r, d)
            else:
                nr, nb = collapse(r, b, d)
            return nr, nb
        # 상으로 기울일 경우
        else:
            if rx < bx:
                nr, nb = collapse(r, b, d)
            else:
                nb, nr = collapse(b, r, d)
            return nr, nb
    else:
        return straight(rx, ry, d), straight(bx, by, d)

def dfs(r, b, pre, cnt):
    if cnt == 10:
        return

    for k in range(4):
        if pre == k:
            continue

        new_R, new_B = move(r, b, k)
        if new_R == hole and new_B != hole:
            print(1)
            exit()
        elif new_B == hole:
            continue
        else:
            dfs(new_R, new_B, k, cnt+1)

n, m = map(int, input().split())
g = [list(input().rstrip()) for _ in range(n)]
red = blue = hole = (0, 0)
for i in range(n):
    for j in range(m):
        if g[i][j] == 'R':
            red = (i, j)
            g[i][j] = '.'
        elif g[i][j] == 'B':
            blue = (i, j)
            g[i][j] = '.'
        elif g[i][j] == 'O':
            hole = (i, j)

dfs(red, blue, -1, 0)
print(0)