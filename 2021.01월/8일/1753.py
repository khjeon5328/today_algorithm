import sys


sys.stdin = open('input.txt')

V, E = map(int, input().split())
K = int(input())
arr = [[] for _ in range(V + 1)]

INF = sys.maxsize
visited = [INF] * (V+1)
visited[0] = 0
visited[K] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append([w, v])

import heapq
q = []
heapq.heappush(q, [0, K])
while q:
    dis, end = heapq.heappop(q)

    for d, x in arr[end]:
        d += dis
        if d < visited[x]:
            visited[x] = d
            heapq.heappush(q, [d, x])
# print(visited)
for i in visited[1:]:
    if i != INF:
        print(i)
    else:
        print('INF')