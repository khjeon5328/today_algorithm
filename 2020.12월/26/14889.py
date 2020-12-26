import sys

sys.stdin = open('input.txt')

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
visited = [0] * N
minV = 987654321

def calc(visited):
    global minV
 
    starV = 0
    linkV = 0

    for i in range(N):
        for j in range(N):
            if visited[i]:
                if visited[j]:
                    starV += arr[i][j]
            else:
                if not visited[j]:
                    linkV += arr[i][j]
    diff = abs(starV - linkV)
    if diff < minV:
        minV = diff




def dfs(n, k, visited):
    global N
    if n == N//2:
        # print(visited)
        calc(visited)
        return
    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(n+1, i+1, visited)
            visited[i] = 0

dfs(0, 0, visited)
print(minV)