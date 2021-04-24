import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque
A, B, N, M = map(int, input().split())
visited = [0] * 100001
visited[N] = 1

def bfs(N, k):
    q = deque([[N, k]])
    while len(q):
        idx, cnt = q.popleft()
        if idx == M:
            return
        
        for i in [idx-1, idx+1, idx+A, idx-A, idx+B, idx-B, idx*A, idx*B]:
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = cnt+1
                q.append([i, cnt + 1])
bfs(N, 0)
print(visited[M])
