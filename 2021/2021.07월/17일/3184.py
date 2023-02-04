import sys
from collections import deque

sys.stdin = open('input.txt')

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

visited = [[0]*C for _ in range(R)]

sheep = 0
wolf = 0

def bfs(y, x):
    global sheep, wolf

    q = deque([(y, x)])

    visited[y][x] = 1
    s = w = 0
    if arr[y][x] == 'v':
        w += 1
    elif arr[y][x] == 'o':
        s += 1


    while q:
        y, x = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and arr[ny][nx] != '#':
                visited[ny][nx] = 1
                if arr[ny][nx] == 'o':
                    s += 1
                elif arr[ny][nx] == 'v':
                    w += 1
                q.append((ny, nx))
    if w >= s:
        wolf += w
    else:
        sheep += s



for y in range(R):
    for x in range(C):
        if not visited[y][x] and arr[y][x] != '#':
            bfs(y, x)
print(sheep, wolf)