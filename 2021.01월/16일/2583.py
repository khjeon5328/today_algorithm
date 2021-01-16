import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

from collections import deque
def bfs(y, x, k):
    arr[y][x] = 1
    q = deque([[y, x]])

    while len(q):
        loc = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny = loc[0] + dy
            nx = loc[1] + dx
            if 0 <= nx < N and 0 <= ny < M and not arr[ny][nx]:
                k += 1
                q.append([ny, nx])
                arr[ny][nx] = 1
    zone.append(k)
    

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            arr[y][x] = 1
# from pprint import pprint
# pprint(arr)
zone = []
for y in range(M):
    for x in range(N):
        if not arr[y][x]:
            bfs(y, x, 1)
zone.sort()
print(len(zone))
print(*zone)