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
    v = k = 0
    if arr[y][x] == 'v':
        v += 1
    elif arr[y][x] == 'k':
        k += 1
    
    while q:
        y, x = q.popleft()
        for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx] and arr[ny][nx] != '#':
                visited[ny][nx] = 1
                if arr[ny][nx] == 'v':
                    v += 1
                elif arr[ny][nx] == 'k':
                    k += 1
                q.append((ny, nx))
    if v >= k:
        wolf += v
    else:
        sheep += k


for y in range(R):
    for x in range(C):
        if arr[y][x] != '#' and not visited[y][x]:
            visited[y][x] = 1
            bfs(y, x)
print(sheep, wolf)