import sys
input = sys.stdin.readline

 def function(g):
     if len(g) == 1:
         return g[0][0]

     d = len(g) // 3
     temp = []
     for i in range(3):
         for j in range(3):
             new = []
             for k in range(d):
                 new.append(g[i*d + k][j*d:j*d+d])
             temp.append(function(new))

     if len(set(temp)) == 1:
         return temp[0]
     else:
         for t in temp:
             if t is not None:
                 result[t] += 1
         return


 N = int(input())
 g = [list(map(int, input().split())) for _ in range(N)]
 result = {-1: 0, 0: 0, 1: 0}
 r = function(g)
 if r is not None:
     result[r] += 1
 for i in range(-1, 2):
     print(result[i])
