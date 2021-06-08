import sys
from pprint import pprint
from collections import deque
from copy import deepcopy

sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# pprint(arr)
cctv_info = []
# print(info)
for y in range(N):
    for x in range(M):
        if arr[y][x] !=6 and arr[y][x]:
            cctv_info.append([y, x, arr[y][x]])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

direction = [
    [],
    [[0], [1], [2], [3]], 
    [[0, 2], [1, 3]], 
    [[0, 1], [1, 2], [2, 3], [3, 0]], 
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]], 
]

def fill(board, d, y, x):
    for i in d:
        ny = y + dy[i]
        nx = x + dx[i]
        while 0<= ny < N and 0<= nx < M and board[ny][nx] != 6:
            if not board[ny][nx]:
                board[ny][nx] = '#'
            ny += dy[i]
            nx += dx[i]
minV = 64

def dfs(board, cctv_cnt):
    global minV, cctv_info

    temp = deepcopy(board)

    if cctv_cnt == len(cctv_info):
        # print()
        # pprint(board)
        cnt = 0
        for y in range(N):
            cnt += board[y].count(0)
        minV = min(cnt, minV)
        return

    y = cctv_info[cctv_cnt][0]
    x = cctv_info[cctv_cnt][1]
    n = cctv_info[cctv_cnt][2]

    for i in direction[n]:
        fill(temp, i, y, x)
        dfs(temp, cctv_cnt + 1)
        temp = deepcopy(board)

# print(cctv_info)
dfs(arr, 0)
print(minV)
