import sys
input = sys.stdin.readline

winner = 0
omoc = [list(map(int, input().rstrip().split())) for _ in range(19)]
direc = [(0, 1), (1, 0),(1, 1),(1, -1)]

def search(x, y, dir, value):
  dx, dy = dir
  cnt = 0
  if 2*abs(dx) <= x < 19 - 2*abs(dx) and 2*abs(dy) <= y < 19 - 2*abs(dy) :
    for i in range(-2,3):
      if omoc[x+dx*i][y+dy*i] == value :
        cnt += 1
    if cnt == 5 :
      if 0 <= x+3*dx < 19 and 0 <= y+3*dy < 19 and omoc[x+3*dx][y+3*dy] == value : 
        return 0
      if 0 <= x-3*dx < 19 and 0 <= y-3*dy < 19 and omoc[x-3*dx][y-3*dy] == value : 
        return 0
      if dy < 0 : dx = -dx
      print(f"{value}\n{x-2*dx+1} {y-2*abs(dy)+1}")
      return 1
  return 0
      
for i in range(19):
  for j in range(19):
    value = omoc[i][j]
    if value != 0 :
      for k in direc :
        if search(i, j, k, value) :
          winner = 1
          break
if not winner : print(0)