import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = 5
arr = [list(map(str , input().split())) for _ in range(N)]

ans = []

def bfs(y, x, k, six):
    six += arr[y][x]

    if k == N:
        if six not in ans:
            ans.append(six)
        return
    
    for dx, dy, in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        ny = y + dy
        nx = x + dx
        if 0 <= nx < N and 0 <= ny < N:
            bfs(ny, nx, k+1, six)


for y in range(N):
    for x in range(N):
        bfs(y, x, 0, '')
# print(ans)
print(len(ans))