import sys


sys.stdin = open('input.txt')

N, M = map(int, input().split())

comb = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    comb[a][b] = 1
    comb[b][a] = 1
# print(comb) 

def check(visited):
    for i in range(1, N+1):
        if visited[i]:
            for j in range(1, N+1):
                if comb[i][j] and visited[j]:
                    return False
    return True

ans = 0
def dfs(k, s, visited):
    global ans
    if k == 3:
        # print(visited)
        if check(visited):
            ans += 1
        return
    for i in range(s, N+1):
        visited[i] = 1
        dfs(k+1, i+1, visited)
        visited[i] = 0

dfs(0, 1, [0]*(N+1))

print(ans)