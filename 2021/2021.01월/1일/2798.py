import sys


sys.stdin = open('input.txt')

n, m = map(int, input().split())
stack = list(map(int, input().split()))
visited = [0] * 3
# print(stack)
ans = 0

def dfs(k, idx, visited):
    global ans
    if ans == m:
        return
        
    if sum(visited) > m:
        return
    
    if k == 3:
        # print(visited)
        black = sum(visited)
        if  black > ans:
            ans = black
        return

    for i in range(idx, n):
        visited[k] = stack[i]
        dfs(k+1, i+1, visited)
        visited[k] = 0

dfs(0, 0, visited)

print(ans)