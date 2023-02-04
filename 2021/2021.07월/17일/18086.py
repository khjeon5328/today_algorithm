import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt')

N, M = map(int, input().split())


arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def bfs(y, x, d):
    global ans

    q = deque([(y, x, d)])
    visited = [[0] * M for _ in range(N)]
    visited[y][x] = 1

    while q:
        y, x, d = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                visited[ny][nx] = d
                if arr[ny][nx] == 1:
                    return d
                else:
                    q.append((ny, nx, d+1)) 
        

for y in range(N):
    for x in range(M):
        if not arr[y][x]:
            ans = max(ans, bfs(y, x, 1))

print(ans)