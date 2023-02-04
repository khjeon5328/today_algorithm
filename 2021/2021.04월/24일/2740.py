import sys

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
m1 = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
m2 = [list(map(int, input().split())) for _ in range(M)]

m3 = [[0]*K for _ in range(N)]

for y in range(N):
    for x in range(K):
        for i in range(M):
            m3[y][x]  += (m1[y][i] * m2[i][x])

for i in m3:
    print(*i)
