import sys

sys.stdin = open('input.txt')

T = int(input())
# T = 1
for _ in range(T):
    k = int(input())
    n = int(input())

    apart = [[i for i in range(n+1)] for _ in range(k+1)]
    for y in range(1, k+1):
        for x in range(1, n+1):
            v = 0
            for i in range(1, x+1):
                v += apart[y-1][i]
            apart[y][x] = v

    print(apart[k][n])