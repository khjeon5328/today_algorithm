import sys
from collections import deque

sys.stdin = open('input.txt')

M, N = map(int , input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)
q = deque()
visited = [[0]*M for _ in range(N)]

flag = False

for y in range(N):
    for x in range(M):
        if arr[y][x] == 0:
            flag = True
            break

if flag:
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                q.append((0, [y, x]))
                visited[y][x] = 1
            elif arr[y][x] == -1:
                visited[y][x] = 1

    while len(q):
        loc = q.popleft()
        day = loc[0]
        cur_y = loc[1][0]
        cur_x = loc[1][1]

        dx = [1, 0, -1, 0]
        dy = [0, -1, 0, 1]
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if 0 <= new_x < M and 0 <= new_y < N and arr[new_y][new_x] == 0:
                arr[new_y][new_x] = 1
                q.append((day+1, [new_y, new_x]))
                visited[new_y][new_x] = day + 1

    # print(visited)

    maxV = 0
    for i in visited:
        if 0 in i:
            print(-1)
            maxV = 0
            break
        else:
            if max(i) > maxV:
                maxV = max(i)
    if maxV:
        print(maxV)

else:
    print(0)
