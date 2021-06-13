import sys

sys.stdin = open('input.txt')

N, K = map(int, input().split())
kit = list(map(int, input().split()))
ans = 0

def comb(weight, n, visited):
    global ans
    if n == N:
        ans += 1
        return
    if weight < 0:
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            comb(weight + kit[i] - K, n + 1, visited)
            visited[i] = 0

comb(0, 0, [0] * N)

print(ans)