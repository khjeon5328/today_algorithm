import sys
from pprint import pprint
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [[[0]*5 for _ in range(N)] for _ in range(N)]

fire = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fire.append((r-1, c-1, m, s, d))

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def move():
    while fire:
        y, x, m, s, d = fire.popleft()
        ny = y + dy[d] * s
        while ny >= N:
            ny -= N
        while ny < 0:
            ny += N
        nx = x + dx[d] * s
        while nx >= N:
            nx -= N
        while nx < 0:
            nx += N
        #질량, 이동, 합쳐친 개수, 방향, 홀짝여부 
        arr[ny][nx][0] += m
        arr[ny][nx][1] += s
        arr[ny][nx][2] += 1
        arr[ny][nx][3] += d
        if arr[ny][nx][4]:
            if arr[ny][nx][4] == 1 and  d % 2 == 0:
                arr[ny][nx][4] = 3
            elif arr[ny][nx][4] == 2 and d % 2 == 1:
                arr[ny][nx][4] = 3
        else:
            if d % 2:
                arr[ny][nx][4] = 1
            else:
                arr[ny][nx][4] = 2
    for y in range(N):
        for x in range(N):
            if arr[y][x][0]:
                if arr[y][x][2] >= 2:
                    nm = arr[y][x][0] // 5
                    if nm:
                        ns = arr[y][x][1] // arr[y][x][2]
                        if arr[y][x][4] == 3:
                            fire.append((y, x, nm, ns, 1))
                            fire.append((y, x, nm, ns, 3))
                            fire.append((y, x, nm, ns, 5))
                            fire.append((y, x, nm, ns, 7))
                        else:
                            fire.append((y, x, nm, ns, 0))
                            fire.append((y, x, nm, ns, 2))
                            fire.append((y, x, nm, ns, 4))
                            fire.append((y, x, nm, ns, 6))
                else:
                    fire.append((y, x, arr[y][x][0], arr[y][x][1], arr[y][x][3]))
                for i in range(5):
                    arr[y][x][i] = 0
                



            
        

for _ in range(K):
    move()

# pprint(arr)
ans = 0
for i in fire:
    ans += i[2]
print(ans)