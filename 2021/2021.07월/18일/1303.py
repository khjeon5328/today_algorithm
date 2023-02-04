import sys
from collections import deque

sys.stdin = open('input.txt')

N, M = map(int, input().split())

arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]

B = W = 0

def bfs(y, x, c):
    global B, W
    visited[y][x] = 1
    q = deque([(y, x, c)])
    cnt = 1
    while q:
        y, x, c = q.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < M and 0 <= nx < N and not visited[ny][nx] and arr[ny][nx] == c:
                visited[ny][nx] = 1
                cnt += 1
                q.append((ny, nx, c))
    if c == 'B':
        B += cnt**2
    else:
        W += cnt**2


for y in range(M):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x, arr[y][x])
print(W, B)