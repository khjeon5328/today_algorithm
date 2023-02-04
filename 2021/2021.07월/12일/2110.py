import sys


sys.stdin = open('input.txt')

N, C = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()
#1, 2, 4, 8, 9
ans = 0
def dfs(n, visited, dist, preV):
    global ans
    if ans:
        if dist <= ans:
            return
    if n == C:
        # print(visited)
        minV = 987654321
        s = 0
        for i in range(N):
            if visited[i]:
                if s:
                    minV = min(minV, lst[i] - s)
                    s = lst[i]
                else:
                    s = lst[i]
        # print(minV, visited)
        ans = max(ans, minV)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            if n == 0:
                dfs(n+1, visited, dist, lst[i])
            else:
                dfs(n+1, visited, min(dist, lst[i] - preV), lst[i])
            visited[i] = 0

dfs(0, [0]*N, 987654321, 0)
# print(lst)
print(ans)