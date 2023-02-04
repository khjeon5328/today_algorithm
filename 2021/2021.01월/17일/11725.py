import sys

# sys.stdin = open('input.txt')
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
# visited[0] = 1
visited[1] = 1
# print(arr)
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx):
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = idx
            dfs(i)

dfs(1)
# print(visited)
for i in visited[2:]:
    print(i)