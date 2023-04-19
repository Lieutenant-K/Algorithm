import sys
input = sys.stdin.readline

N = int(input())
square = set([i*i for i in range(1, N+1)])

if N in square:
    print(1)
    exit()

for x in range(1, int(N**0.5)+1):
    if(N - x*x) in square:
        print(2)
        exit()
for y in range(1, int(N**0.5)+1):
    for z in range(1, int(N**0.5)+1):
        if(N - y*y - z*z) in square:
            print(3)
            exit()

print(4)