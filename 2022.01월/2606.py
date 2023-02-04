import queue
import sys
from collections import deque

sys.stdin = open('input.txt')

N = int(input())
l = int(input())

arr = [[0] * (N+1) for _ in range(N+1)]

for i in range(l):
    y, x = map(int, input().split())
    arr[y][x] = 1
    arr[x][y] = 1

#print(arr)
cnt = 0
visited = [0] * (N+1)

def bfs():
    global cnt
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        tmp = q.popleft()
        for i in range(1, N+1):
            if arr[tmp][i] and not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1
bfs()
print(cnt)



