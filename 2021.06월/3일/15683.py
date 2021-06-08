import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

pprint(arr)
info = [[] for _ in range(7)]
# print(info)
for y in range(N):
    for x in range(M):
        if arr[y][x]:
            info[arr[y][x]].append((y, x, 0))

from collections import deque
def bfs(info, i):
    q = deque(info)
    dx = [0, 1, 0, -1, 0]
    dy = [0, 0, -1, 0, 1]
    if i == 5:
        while q:
            y, x, d = q.popleft()
            if not d:
                for i in range(1, 5):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and (not arr[ny][nx] or arr[ny][nx] == '#'):
                        arr[ny][nx] = '#'
                        q.append((ny, nx, i))
            else:
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < N and 0 <= nx < M and (not arr[ny][nx] or arr[ny][nx] == '#'):
                    arr[ny][nx] = '#'
                    q.append((ny, nx, d))
    elif i == 4:
        while q:
            y, x, d = q.popleft()
            if not d:
                pass
    elif i == 3:
        pass
    elif i == 2:
        pass
    elif i == 1:
        pass

for i in range(5, 0, -1):
    if info[i]:
        bfs(info[i], i)
pprint(arr)