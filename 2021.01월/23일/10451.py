import sys


sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    # print(arr)
    visited = [0] * (N+1)
    ans = 0

    def dfs(i):
        visited[i] = 1
        if not visited[arr[i]]:
            dfs(arr[i])

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)