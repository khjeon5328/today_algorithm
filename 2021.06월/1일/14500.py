import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# pprint(arr)
maxV = 0

def dfs(y, x, hap, n):
    global maxV, visited

    if n >= 3:
        maxV = max(maxV, hap)
        return


    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = 1
            dfs(ny, nx, hap + arr[ny][nx], n + 1)
            visited[ny][nx] = 0

from itertools import combinations

def check(y, x):
    global maxV

    for comb1 in list(combinations([(1, 0), (-1, 0), (0, 1), (0, -1)], 3)):
        hap = arr[y][x]
        for dx, dy in comb1:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N:
                hap += arr[ny][nx]
            else:
                break
        maxV = max(hap, maxV)
    




visited = [[0] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        dfs(y, x, arr[y][x], 0)
        visited[y][x] = 0
        check(y, x)
        
print(maxV)