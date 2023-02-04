import sys


sys.stdin = open('input.txt')

N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)
path = [V]
def dfs(s, visited):
    global path

    for i in range(N+1):
        if graph[s][i] == 1 and not visited[i]:
            path.append(i)
            visited[i] = 1
            dfs(i, visited)
        

visited = [0]*(N+1)
visited[V] = 1
dfs(V, visited)
print(*path)


from collections import deque

def bfs():
    ans = []

    q = deque([V])
    visited = [0] * (N+1)
    visited[V] = 1

    while len(q):
        s = q.popleft()
        ans.append(s)
        for i in range(N+1):
            if graph[s][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
    print(*ans)
bfs()