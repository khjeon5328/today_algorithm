import sys
from pprint import pprint
from collections import deque

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

cloud = deque()
cloud.append((N-1, 0))
cloud.append((N-1, 1))
cloud.append((N-2, 0))
cloud.append((N-2, 1))
# print(cloud)

def bfs(d, s):
    visited = [[0]*N for _ in range(N)]
    for _ in range(len(cloud)):
        y, x = cloud.popleft()

        ny = y + (dy[d] * s)
        while ny >= N:
            ny -= N
        while ny < 0:
            ny += N

        nx = x + (dx[d] * s)
        while nx >= N:
            nx -= N
        while nx < 0:
            nx += N
        # print(ny, nx)
        arr[ny][nx] += 1
        visited[ny][nx] = 1
        cloud.append((ny, nx))

    while cloud:
        ny, nx = cloud.popleft()
        cnt = 0
        for cx, cy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            ax = nx + cx
            ay = ny + cy
            if 0<= ax < N and 0<= ay < N and arr[ay][ax]:
                cnt += 1
        arr[ny][nx] += cnt

    for y in range(N):
        for x in range(N):
            if not visited[y][x] and arr[y][x] >= 2:
                arr[y][x] -= 2
                cloud.append((y, x))


for i in range(M):
    # if i == 2:
    #     break
    d, s = map(int, input().split())
    bfs(d-1, s)
# pprint(arr)
ans = 0
for y in range(N):
    ans += sum(arr[y])
print(ans)