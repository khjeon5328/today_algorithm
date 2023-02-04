import sys

sys.stdin = open('input.txt')

# input = sys.stdin.readline()

N, M = map(int, input().split())

visited = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
def dfs(k):
    global visited, graph

    visited[k] = 1

    for i in graph[k]:
        if not visited[i]:
            dfs(i)

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)