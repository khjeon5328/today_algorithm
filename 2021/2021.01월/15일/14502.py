import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
virus_lst = []
for y in range(N):
    for x in range(M):
        if arr[y][x] == 2:
            virus_lst.append([y, x])

maxV = 0
def select_wall(k, start):
    global maxV

    if k == 3:
        cnt = spread_virus(arr)
        maxV = max(maxV, cnt)
        return

    for i in range(start, N*M):
        ny = i // M
        nx = i % M
        if arr[ny][nx] == 0:
            arr[ny][nx] = 1
            select_wall(k+1, i+1)
            arr[ny][nx] = 0

from collections import deque
import copy
def spread_virus(arr):
    check_arr = copy.deepcopy(arr)
    q = deque() 
    for virus in virus_lst:
        q.append(virus)

    while len(q):
        virus = q.popleft()
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny = virus[0] + dy
            nx = virus[1] + dx
            if 0<= ny < N and 0 <= nx < M and not check_arr[ny][nx]:
                check_arr[ny][nx] = 2
                q.append([ny, nx])
    cnt = 0
    for i in range(N):
        cnt += check_arr[i].count(0)
    return cnt


select_wall(0, 0)
print(maxV)
# spread_virus(arr)