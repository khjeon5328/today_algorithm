import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt')

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
def move(y, x, visited, isMove):
    cities = deque()
    hap = arr[y][x]
    cities.append((y, x))
    q = deque()
    q.append((y, x))
    visited[y][x] = 1

    while q:
        y, x = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and L <= abs(arr[y][x] - arr[ny][nx]) <= R and not visited[ny][nx]:
                cities.append((ny, nx))
                q.append((ny, nx))
                hap += arr[ny][nx]
                visited[ny][nx] = 1
    avg = hap // len(cities)

    if not isMove:
        if len(cities) >= 2:
            isMove = True
    
    while cities:
        y, x = cities.popleft()
        arr[y][x] = avg

    return isMove

def check():
    # for i in range(N):
    #     print(arr[i])
    # print()
    global ans

    visited = [[0]*N for _ in range(N)]
    isMove = False
    for y in range(N):
        for x in range(N):
            # print(y, x, visited)
            if not visited[y][x]:
                isMove = move(y, x, visited, isMove)
    if isMove:        
        ans += 1
        check()

check()
print(ans)
# print(arr)