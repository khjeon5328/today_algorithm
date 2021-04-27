import sys
from pprint import pprint

sys.stdin = open('input.txt')

input = sys.stdin.readline

M, N, H = map(int, input().split())

arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# pprint(arr)
from collections import deque

def calc(visited):
    maxV = 1
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if visited[i][j][k] == 0:
                    print(-1)
                    return 
                elif visited[i][j][k] > maxV:
                    maxV = visited[i][j][k]
    print(maxV)

def bfs():
    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 1:
                    q.append((i, j, k, 0))
                    visited[i][j][k] = 1
                elif arr[i][j][k] == -1:
                    visited[i][j][k] = -1
    # print(q)
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, -1, 0, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while q:
        h, n, m, day = q.popleft()

        for i in range(6):
            nh = h + dz[i]
            nn = n + dy[i]
            nm = m + dx[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and not arr[nh][nn][nm] and not visited[nh][nn][nm]: 
                visited[nh][nn][nm] = day + 1
                q.append((nh, nn, nm, day + 1))
    # pprint(visited)
    calc(visited)

def checkNullBox():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if arr[i][j][k] == 0:
                    return True
                    


if checkNullBox():
    bfs()
else:
    print(0)